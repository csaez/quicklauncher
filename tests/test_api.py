# The MIT License (MIT)

# Copyright (c) 2014 Cesar Saez

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import mock
import unittest
from collections import Iterable

import quicklauncher as ql

_REPO = ql.api.get_repo()


class MiscCase(unittest.TestCase):
    def test_show(self):
        self.assertIsNotNone(ql.show)

    def test_list_scripts(self):
        self.assertIsInstance(ql.api.list_scripts(), Iterable)
        self.assertIsInstance(ql.api.get_scripts(), dict)
        self.assertEqual(len(ql.api.list_scripts()), len(ql.api.get_scripts()))

    def test_list_commands(self):
        with mock.patch("quicklauncher.api.cmds", create=True):
            self.assertIsInstance(ql.api.list_commands(), Iterable)
            self.assertIsInstance(ql.api.get_commands(), dict)
            self.assertEqual(len(ql.api.list_commands()),
                             len(ql.api.get_commands()))

    def test_run_cmd(self):
        with mock.patch("quicklauncher.api.cmds", create=True):
            self.assertTrue(ql.api.run_cmd("ls"))


class RepoCase(unittest.TestCase):
    def setUp(self):
        test_path = os.path.join(os.path.expanduser("~"), "testing")
        ql.api.set_repo(test_path)

    def tearDown(self):
        ql.api.set_repo(_REPO)
        test_path = os.path.join(os.path.expanduser("~"), "testing")
        os.rmdir(test_path)

    def test_repo(self):
        test_path = os.path.join(os.path.expanduser("~"), "testing")
        self.assertEqual(ql.api.get_repo(), test_path)
        self.assertTrue(os.path.isdir(ql.api.get_repo()))
        self.assertEqual(ql.api.get_repo(), test_path)


class ScriptCase(unittest.TestCase):
    def setUp(self):
        test_path = os.path.join(os.path.expanduser("~"), "testing")
        ql.api.set_repo(test_path)

        with open(os.path.join(ql.api.get_repo(), "testsuite.py"), "w") as f:
            code = 'print("im in the root dir")'
            f.write(code)
        subdir = os.path.join(ql.api.get_repo(), "test")
        if not os.path.exists(subdir):
            os.mkdir(subdir)
        with open(os.path.join(subdir, "testsuite.py"), "w") as f:
            code = 'print("im in a subdir")'
            f.write(code)

    def tearDown(self):
        for x in ("testsuite.py", "testsuite.pyc"):
            path = os.path.join(ql.api.get_repo(), x)
            if os.path.exists(path):
                os.remove(path)
        subdir = os.path.join(ql.api.get_repo(), "test")
        for x in ("testsuite.py", "testsuite.pyc"):
            path = os.path.join(subdir, x)
            if os.path.exists(path):
                os.remove(path)
        os.rmdir(subdir)

        ql.api.set_repo(_REPO)
        test_path = os.path.join(os.path.expanduser("~"), "testing")
        os.rmdir(test_path)

    def test_run_script(self):
        self.assertTrue(ql.api.run_script("testsuite.py"))
        self.assertTrue(ql.api.run_script("test/testsuite.py"))


if __name__ == "__main__":
    unittest.main(verbosity=3)
