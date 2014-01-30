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
import json
from collections import OrderedDict

from wishlib.si import si


class Manager(object):

    def __init__(self):
        super(Manager, self).__init__()
        self.HOME_DIR = os.path.join(os.path.expanduser("~"), "quicklauncher")
        self.HOME_DIR = os.path.normpath(self.HOME_DIR)
        if not os.path.exists(self.HOME_DIR):
            os.makedirs(self.HOME_DIR)
        self.PREF_FILE = os.path.join(self.HOME_DIR, "preferences.json")
        self.CACHE_FILE = os.path.join(self.HOME_DIR, "cache.json")

    def scan(self):
        data = dict()
        # get all softimage commands without arguments or with default values
        for cmd in si.Commands:
            if not cmd.Arguments.Count or all([arg.Value for arg in cmd.Arguments]):
                cmd_name = str(cmd.Name)
                data[cmd_name] = cmd_name
        # get custom scripts
        EXCEPTIONS = ["README.md"]
        for root, dirnames, filenames in os.walk(self.script_dir):
            if ".git" in root:
                continue
            for filename in filenames:
                script = os.path.join(root, filename)
                validation = [os.path.isfile(script),
                              not filename.startswith("."),
                              filename not in EXCEPTIONS]
                if all(validation):
                    # include package reference on key
                    key = script.replace(self.script_dir, "")[1:]
                    data[key] = script
        # save to file
        with open(self.CACHE_FILE, "w") as f:
            json.dump(data, f)
        return data

    def find(self, word):
        index = 0
        result = list()
        for key in self.data.keys():
            if word.lower() not in key.lower():
                continue
            result.append(key)
            index += 1
            if index >= self.limit:
                break
        return result

    @property
    def data(self):
        if hasattr(self, "_data"):
            return self._data
        try:
            # read from cache file
            with open(self.CACHE_FILE) as f:
                data = json.load(f)
        except:
                data = self.scan()
        # sort and return
        self._data = OrderedDict(sorted(data.items(),
                                        key=lambda x: x[0].lower()))
        return self._data

    @property
    def preferences(self):
        if hasattr(self, "_preferences"):
            return self._preferences
        try:
            # read from cache file
            with open(self.PREF_FILE) as f:
                self._preferences = json.load(f)
        except:
            # use default values
            self._preferences = {}
            script_dir = os.path.join(self.HOME_DIR, "scripts")
            if not os.path.exists(script_dir):
                os.makedirs(script_dir)
            self._preferences["script_dir"] = script_dir
            self._preferences["limit"] = 8
            # save to file
            self._saveprefs()
        return self._preferences

    @property
    def script_dir(self):
        return self.preferences.get("script_dir")

    @script_dir.setter
    def script_dir(self, value):
        self.preferences["script_dir"] = value
        if not os.path.exists(value):
            os.makedirs(value)
        self._saveprefs()
        self.scan()

    @property
    def limit(self):
        return self.preferences.get("limit")

    @limit.setter
    def limit(self, value):
        self.preferences["limit"] = value
        self._saveprefs()

    def _saveprefs(self):
        with open(self.PREF_FILE, "w") as f:
            json.dump(self.preferences, f, indent=4)

    def execute(self, key):
        code = self.data.get(key)
        if os.path.isfile(code):
            si.ExecuteScript(code)
        else:
            si.Commands(code).Execute()
