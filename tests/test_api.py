import os
import mock
import unittest
from collections import Iterable

import quicklauncher as ql

_REPO = ql.get_repo()


class MiscCase(unittest.TestCase):
    def test_show(self):
        self.assertIsNotNone(ql.show)

    def test_list_scripts(self):
        self.assertIsInstance(ql.list_scripts(), Iterable)
        self.assertIsInstance(ql.get_scripts(), dict)
        self.assertEqual(len(ql.list_scripts()), len(ql.get_scripts()))

    def test_list_commands(self):
        with mock.patch("maya.cmds", create=True):
            self.assertIsInstance(ql.list_commands(), Iterable)
            self.assertIsInstance(ql.get_commands(), dict)
            self.assertEqual(len(ql.list_commands()),
                             len(ql.get_commands()))

    def test_run_cmd(self):
        with mock.patch("maya.cmds", create=True):
            self.assertTrue(ql.run_cmd("ls"))


class RepoCase(unittest.TestCase):
    def setUp(self):
        test_path = os.path.join(os.path.expanduser("~"), "testing")
        ql.set_repo(test_path)

    def tearDown(self):
        ql.set_repo(_REPO)
        test_path = os.path.join(os.path.expanduser("~"), "testing")
        os.rmdir(test_path)

    def test_repo(self):
        test_path = os.path.join(os.path.expanduser("~"), "testing")
        self.assertEqual(ql.get_repo(), test_path)
        self.assertTrue(os.path.isdir(ql.get_repo()))
        self.assertEqual(ql.get_repo(), test_path)


class ScriptCase(unittest.TestCase):
    def setUp(self):
        test_path = os.path.join(os.path.expanduser("~"), "testing")
        ql.set_repo(test_path)

        with open(os.path.join(ql.get_repo(), "testsuite.py"), "w") as f:
            code = 'print("im in the root dir")'
            f.write(code)
        subdir = os.path.join(ql.get_repo(), "test")
        if not os.path.exists(subdir):
            os.mkdir(subdir)
        with open(os.path.join(subdir, "testsuite.py"), "w") as f:
            code = 'print("im in a subdir")'
            f.write(code)

    def tearDown(self):
        for x in ("testsuite.py", "testsuite.pyc"):
            path = os.path.join(ql.get_repo(), x)
            if os.path.exists(path):
                os.remove(path)
        subdir = os.path.join(ql.get_repo(), "test")
        for x in ("testsuite.py", "testsuite.pyc"):
            path = os.path.join(subdir, x)
            if os.path.exists(path):
                os.remove(path)
        os.rmdir(subdir)

        ql.set_repo(_REPO)
        test_path = os.path.join(os.path.expanduser("~"), "testing")
        os.rmdir(test_path)

    def test_run_script(self):
        self.assertTrue(ql.run_script("testsuite.py"))
        self.assertTrue(ql.run_script("test/testsuite.py"))


if __name__ == "__main__":
    unittest.main(verbosity=3)
