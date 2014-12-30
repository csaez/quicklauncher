from . import lib
from PySide import QtCore, QtGui


class QuickLauncher(QtGui.QMenu):

    """A menu to find and execute Maya commands and user scripts."""

    def __init__(self, *args, **kwds):
        super(QuickLauncher, self).__init__(*args, **kwds)
        self.init_gui()

    def init_gui(self):
        # set search field
        self.lineEdit = QtGui.QLineEdit(self)
        action = QtGui.QWidgetAction(self)
        action.setDefaultWidget(self.lineEdit)
        self.addAction(action)
        self.lineEdit.setFocus()
        # completion
        items = lib.list_scripts()
        items.extend(lib.list_commands())
        completer = QtGui.QCompleter(items, self)
        completer.setCompletionMode(QtGui.QCompleter.PopupCompletion)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.lineEdit.setCompleter(completer)
        # connect signals
        self.lineEdit.returnPressed.connect(self.accept)

    def accept(self):
        text = self.lineEdit.text()
        self.close()
        if not lib.run_cmd(text):
            lib.run_script(text)


def select_repo():
    repo = QtGui.QFileDialog.getExistingDirectory(
        caption="Select repository directory",
        parent=lib.get_parent(),
        dir=lib.get_repo())
    if repo:
        lib.set_repo(repo)


def setup_hotkey():
    """Assign TAB-key to open quicklauncher"""
    hotkey_sequence = QtGui.QKeySequence(QtCore.Qt.Key_Tab)
    hotkey_log = QtGui.QShortcut(hotkey_sequence, lib.get_parent())
    hotkey_log.activated.connect(show)


def show():
    maya_window = lib.get_parent()
    # look for existing instances of QuickLauncher
    ql = get_instance(maya_window, QuickLauncher)
    if ql is None:
        # create a new instance
        ql = QuickLauncher(maya_window)
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
