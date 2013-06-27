from wishlib.si import C, log, show_qt
from PyQt4 import QtGui


def XSILoadPlugin(in_reg):
    in_reg.Author = "csaez"
    in_reg.Name = "QuickLauncherPlugin"
    in_reg.Major = 1
    in_reg.Minor = 0
    in_reg.RegisterCommand("QuickLauncher", "QuickLauncher")
    in_reg.RegisterCommand("QuickLauncher_Reloader", "QuickLauncher_Reloader")
    return True


def XSIUnloadPlugin(in_reg):
    log("{} has been unloaded.".format(in_reg.Name), C.siVerbose)
    return True


def QuickLauncher_Execute():
    log("QuickLauncher_Execute called", C.siVerbose)
    from quicklauncher.layout.menu import Menu
    pos = QtGui.QCursor.pos()
    show_qt(Menu, modal=True, onshow_event=lambda x: x.move(pos.x(), pos.y()))


def QuickLauncher_Reloader_Execute():
    log("QuickLauncher_Reloader_Execute called", C.siVerbose)
    from quicklauncher import manager
    manager.get_data(False)  # reload cache on disk
    return True
