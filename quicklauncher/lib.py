"""Helper functions"""

import os
import sys
import inspect

from PySide import QtCore, QtGui
from shiboken import wrapInstance

from maya import cmds
from maya import OpenMayaUI


__all__ = ['get_parent',
           'get_repo',
           'set_repo',
           'list_scripts',
           'get_scripts',
           'list_commands',
           'get_commands',
           'run_script',
           'run_cmd']


class CaseInsensitiveDict(dict):

    def get(self, name, **kwds):
        for k in self.keys():
            if name.lower() == k.lower():
                return self.__getitem__(k)
        return super(CaseInsensitiveDict, self).get(name, **kwds)


def get_parent():
    """Return main window as QObject"""
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(ptr), QtGui.QMainWindow)


def get_repo():
    settings = QtCore.QSettings("csaez", "quicklauncher")
    repo = settings.value("repo")
    if not repo:
        repo = os.path.join(os.path.expanduser("~"), "quicklauncher")
        set_repo(repo)
    return repo


def set_repo(repo_path):
    if not os.path.exists(repo_path):
        os.mkdir(repo_path)
    settings = QtCore.QSettings("csaez", "quicklauncher")
    settings.setValue("repo", repo_path)


def get_scripts():  # {name: path, ...}
    items = [os.path.join(path, f)
             for (path, _, files) in os.walk(get_repo())
             for f in files if f.endswith(".py")]
    return dict(((x.replace("%s/" % get_repo(), ""), x) for x in items))


def list_scripts():
    return get_scripts().keys()


def get_commands():  # {name: cmd, ...}
    items = [x for x in inspect.getmembers(cmds, callable)]
    return CaseInsensitiveDict(items)


def list_commands():
    return get_commands().keys()


def run_script(script_name):
    # validate
    script_path = get_scripts().get(script_name)
    if not script_path:
        return False
    # add to pythonpath and execute
    sys.path.append(os.path.dirname(script_path))
    module_name = os.path.split(script_path)[-1].replace(".py", "")
    __import__(module_name)
    # cleanup
    del sys.modules[module_name]
    sys.path = sys.path[:-1]
    return True


def run_cmd(cmd_name):
    cmd = get_commands().get(cmd_name)
    if cmd is not None:
        cmd()
        return True
    return False
