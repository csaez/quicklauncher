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
import inspect
from . import interface
import pymel.core.runtime as cmds


class Manager(interface.Manager):

    def get_cmds(self):
        return dict([(x, x) for x, _ in inspect.getmembers(cmds, callable)])

    def execute(self, key):
        v = self.data.get(key)
        if os.path.isfile(v):
            fp = os.path.join(self.script_dir, v)
            with open(fp) as f:
                code = f.read()
            exec(code)
        else:
            getattr(cmds, v)()
