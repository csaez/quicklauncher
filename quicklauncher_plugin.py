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

from wishlib.si import C, log, show_qt


def XSILoadPlugin(in_reg):
    in_reg.Author = "csaez"
    in_reg.Name = "QuickLauncher Plugin"
    in_reg.Major = 1
    in_reg.Minor = 0
    in_reg.RegisterCommand("QuickLauncher", "QuickLauncher")
    in_reg.RegisterCommand("QuickLauncher Reloader", "QuickLauncher_Reloader")
    in_reg.RegisterCommand("QuickLauncher Preferences",
                           "QuickLauncher_Preferences")
    in_reg.RegisterEvent("QuickLauncher_Startup", C.siOnStartup)
    return True


def XSIUnloadPlugin(in_reg):
    log("{} has been unloaded.".format(in_reg.Name), C.siVerbose)
    return True


def QuickLauncher_Execute():
    log("QuickLauncher_Execute called", C.siVerbose)
    from quicklauncher.layout.menu import Menu
    from wishlib.qt import QtGui
    pos = QtGui.QCursor.pos()
    show_qt(Menu, modal=True, onshow_event=lambda x: x.move(pos.x(), pos.y()))


def QuickLauncherReloader_Execute():
    log("QuickLauncherReloader_Execute called", C.siVerbose)
    from quicklauncher.manager import Manager
    Manager().scan()  # reload cache on disk
    return True


def QuickLauncherPreferences_Execute():
    log("QuickLauncherPreferences_Execute called", C.siVerbose)
    from quicklauncher.layout.prefs import Prefs
    show_qt(Prefs)
    return True


def QuickLauncher_Startup_OnEvent(in_ctxt):
    log("QuickLauncher_Startup_OnEvent called", C.siVerbose)
    Application.QuickLauncher_Reloader()
    return True
