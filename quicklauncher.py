from wishlib.qt.QtGui import QCursor
from quicklauncher.layout.menu import Menu
from wishlib import inside_softimage, inside_maya
if inside_softimage():
    from wishlib.si import show_qt
elif inside_maya():
    from wishlib.ma import show_qt


pos = QCursor.pos()
show_qt(Menu, modal=True, onshow_event=lambda x: x.move(pos.x(), pos.y()))
