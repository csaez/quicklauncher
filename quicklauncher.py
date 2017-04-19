# The MIT License (MIT)

# Copyright (c) 2014 Cesar Saez

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import sys
import inspect
from importlib import import_module
import maya.cmds as cmds

# qt bindings
try:
    from PySide2 import QtCore, QtGui, QtWidgets
except ImportError:
    from PySide import QtCore, QtGui
    QtWidgets = QtGui


__all__ = ['show', 'get_main_window', 'get_repo', 'set_repo', 'list_scripts',
           'get_scripts', 'list_commands', 'get_commands', 'run_script',
           'run_cmd']


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
    items = [(name.lower(), value)
             for (name, value) in inspect.getmembers(cmds, callable)]
    return dict(items)


def list_commands():
    return get_commands().keys()


def run_script(script_name):
    # validate
    script_path = get_scripts().get(script_name)
    if not script_path:
        return False
    # add to pythonpath and execute
    sys.path.insert(0, os.path.dirname(script_path))
    module_name = os.path.split(script_path)[-1].replace(".py", "")
    import_module(module_name)
    # cleanup
    del sys.modules[module_name]
    sys.path = sys.path[1:]
    return True


def run_cmd(cmd_name):
    cmd = get_commands().get(cmd_name.lower())
    if cmd is not None:
        cmd()
        return True
    return False


# GUI
class QuickLauncherMenu(QtWidgets.QMenu):

    """A menu to find and execute Maya commands and user scripts."""

    def __init__(self, *args, **kwds):
        super(QuickLauncherMenu, self).__init__(*args, **kwds)
        self.init_gui()

    def init_gui(self):
        # set search field
        self.lineEdit = QtWidgets.QLineEdit(self)
        action = QtWidgets.QWidgetAction(self)
        action.setDefaultWidget(self.lineEdit)
        self.addAction(action)
        self.lineEdit.setFocus()
        # completion
        items = list_scripts()
        items.extend(list_commands())
        completer = QtWidgets.QCompleter(items, self)
        completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.lineEdit.setCompleter(completer)
        # connect signals
        self.lineEdit.returnPressed.connect(self.accept)

    def accept(self):
        text = self.lineEdit.text()
        completion = self.lineEdit.completer().currentCompletion()
        self.close()
        return run_cmd(text) or \
            run_cmd(completion) or \
            run_script(text) or \
            run_script(completion)


def select_repo():
    repo = QtWidgets.QFileDialog.getExistingDirectory(
        caption="Select repository directory",
        parent=get_main_window(),
        dir=get_repo())
    if repo:
        set_repo(repo)


def get_main_window(widget=None):
    widget = widget or QtWidgets.QApplication.activeWindow()
    if widget is None:
        return
    parent = widget.parent()
    if parent is None:
        return widget
    return get_main_window(parent)


def show():
    maya_window = get_main_window()
    # look for existing instances of QuickLauncher
    ql = get_instance(maya_window, QuickLauncherMenu)
    if ql is None:
        # create a new instance
        ql = QuickLauncherMenu(maya_window)
    # clear out, move and show
    ql.lineEdit.setText("")
    position_window(ql)
    ql.exec_()


def position_window(window):
    """Position window to mouse cursor"""
    pos = QtGui.QCursor.pos()
    window.move(pos.x(), pos.y())


def get_instance(parent, gui_class):
    for children in parent.children():
        if isinstance(children, gui_class):
            return children
    return None
