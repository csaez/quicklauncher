from wishlib.qt.QtGui import QMenu
from PyQt4 import QtGui
from .. import manager


class Menu(QMenu):

    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        # set the menu as active window
        self.activateWindow()
        # instanciate quicklauncher manager
        self.manager = manager.Manager()
        # add filter lineedit
        self.filter_lineEdit = QtGui.QLineEdit()
        action = QtGui.QWidgetAction(self)
        action.setDefaultWidget(self.filter_lineEdit)
        # populate menu
        self.addAction(action)
        self.items = [self.addAction(x) for x in self.manager.data.keys()]
        self.more_label = self.addAction("More...")
        self.more_label.setDisabled(True)
        # set focus
        self.filter_lineEdit.setFocus()
        # filter items
        self.filter_changed()
        # connect signals to slots
        self.filter_lineEdit.textChanged.connect(self.filter_changed)
        self.filter_lineEdit.returnPressed.connect(self.execute_filtered)
        self.triggered.connect(self.execute_trigger)

    # SLOTS
    def filter_changed(self, name=""):
        # get matches
        matched = self.manager.find(str(name))
        for item in self.items:
            item.setVisible(str(item.text()) in matched)
        self.more_label.setVisible(len(matched) >= self.manager.limit)

    def execute_filtered(self):
        for x in self.children():
            if all([isinstance(x, QtGui.QAction), x.isVisible(), len(x.text())]):
                self.execute_trigger(x)
                return
        self.close()

    def execute_trigger(self, action):
        key = str(action.text())
        self.manager.execute(key)
