import os
import sys
import inspect

try:
    from PySide import QtCore
except ImportError:
    pass

try:
    from maya import cmds
except ImportError:
    pass


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
    return dict(items)


def list_commands():
    return get_commands().keys()


def run_script(script_name):
    # validate
    script_path = get_scripts().get(script_name)
    if not script_path:
        return False
    # add to pythonpath and execute
    if os.path.dirname(script_path) not in sys.path:
        sys.path.append(os.path.dirname(script_path))
    module_name = os.path.split(script_path)[-1].replace(".py", "")
    __import__(module_name)
    # cleanup
    del sys.modules[module_name]
    sys.path = sys.path[:-1]
    return True


def run_cmd(cmd_name):
    commands = get_commands()
    if commands.get(cmd_name):
        commands[cmd_name]()
        return True
    return False
