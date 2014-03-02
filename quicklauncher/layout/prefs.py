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

import os
from wishlib import inside_softimage, inside_maya
from wishlib.qt import QtGui, loadUiType
from ..manager import Manager

ui_file = os.path.join(os.path.dirname(__file__), "ui", "prefs.ui")
form, base = loadUiType(ui_file)


class PrefsInterface(form, base):

    def __init__(self, parent=None):
        super(PrefsInterface, self).__init__(parent)
        self.setupUi(self)
        icon = os.path.join(os.path.dirname(__file__), "ui", "images",
                            "folder_open_icon&16.png")
        self.scripts_button.setIcon(QtGui.QIcon(icon))
        # connect signals
        self.scripts_button.clicked.connect(self.scripts_clicked)
        self.limit_spinBox.valueChanged.connect(self.limit_changed)
        # get manager and set values
        self.manager = Manager()
        self.limit_spinBox.setValue(self.manager.limit)
        self.scripts_lineEdit.setText(self.manager.script_dir)

    def limit_changed(self, value):
        self.manager.limit = value

    def scripts_clicked(self):
        script_dir = str(QtGui.QFileDialog.getExistingDirectory(
            self, "Scripts directory", self.manager.script_dir))
        if len(script_dir):
            self.manager.script_dir = script_dir
            self.scripts_lineEdit.setText(script_dir)

if inside_softimage():
    from wishlib.si import si

    class Prefs(PrefsInterface):

        def scripts_clicked(self):
            si.Desktop.SuspendWin32ControlsHook()
            super(Prefs, self).scripts_clicked()
            si.Desktop.RestoreWin32ControlsHook()

elif inside_maya():
    class Prefs(PrefsInterface):
        pass
