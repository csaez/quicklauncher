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

import os
from wishlib.si import si
from . import interface


class Manager(interface.Manager):

    def get_cmds(self):
        data = dict()
        # get all softimage commands without arguments or with default values
        for cmd in si.Commands:
            if not cmd.Arguments.Count or all([arg.Value for arg in cmd.Arguments]):
                cmd_name = str(cmd.Name)
                data[cmd_name] = cmd_name
        return data

    def execute(self, key):
        code = self.data.get(key)
        if os.path.isfile(code):
            si.ExecuteScript(code)
        else:
            si.Commands(code).Execute()
