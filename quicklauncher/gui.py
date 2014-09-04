from . import api

try:
    from PySide import QtCore, QtGui
    from shiboken import wrapInstance
except ImportError:
    class QtGui:
        QMenu = object

try:
    from maya import OpenMayaUI
except ImportError:
    pass


class QuickLauncher(QtGui.QMenu):

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
        items = api.list_scripts()
        items.extend(api.list_commands())
        completer = QtGui.QCompleter(items, self)
        completer.setCompletionMode(QtGui.QCompleter.PopupCompletion)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.lineEdit.setCompleter(completer)
        # connect signals
        self.lineEdit.returnPressed.connect(self.accept)

    def accept(self):
        text = self.lineEdit.text()
        self.close()
        if not api.run_cmd(text):
            api.run_script(text)


def get_parent():
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(ptr), QtGui.QMainWindow)


def show():
    m = QuickLauncher(parent=get_parent())
    pos = QtGui.QCursor.pos()
    m.move(pos.x(), pos.y())
    m.exec_()
    del m


def select_repo():
    repo = QtGui.QFileDialog.getExistingDirectory(
        parent=get_parent(), caption="Select repository directory",
        dir=api.get_repo())
    if repo:
        api.set_repo(repo)
