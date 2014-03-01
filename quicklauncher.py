from wishlib import show_qt
from wishlib.qt.QtGui import QCursor
from quicklauncher.layout.menu import Menu

pos = QCursor.pos()
show_qt(Menu, modal=True, onshow_event=lambda x: x.move(pos.x(), pos.y()))
