# This file is part of quicklauncher.
# Copyright (C) 2014  Cesar Saez

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation version 3.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import

from wishlib import inside_softimage, inside_maya
from wishlib.qt import QtGui
from ..manager import Manager


class MenuInterface(QtGui.QMenu):

    def __init__(self, parent=None):
        super(MenuInterface, self).__init__(parent)
        # set the menu as active window
        self.activateWindow()
        # instanciate quicklauncher manager
        self.manager = Manager()
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
        self.close()
        self.manager.execute(key)

if inside_softimage():
    class Menu(MenuInterface):
        pass

elif inside_maya():
    class Menu(MenuInterface):

        def __init__(self, parent):
            super(Menu, self).__init__(parent)
            self.manager.scan()
