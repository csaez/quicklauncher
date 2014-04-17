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

from wishlib import show_qt
from wishlib.qt.QtGui import QCursor
from .manager import Manager
from .layout.menu import Menu
from .layout.prefs import Prefs


def show():
    pos = QCursor.pos()
    show_qt(Menu, modal=True, onshow_event=lambda x: x.move(pos.x(), pos.y()))


def prefs():
    show_qt(Prefs)


def reload():
    Manager().scan()
