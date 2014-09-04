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
from nose import with_setup
from collections import Iterable
import quicklauncher as ql


_REPO = ql.api.get_repo()


def test_show():
    assert ql.show is not None


def setup_repo():
    test_path = os.path.join(os.path.expanduser("~"), "testing")
    ql.api.set_repo(test_path)


def teardown_repo():
    ql.api.set_repo(_REPO)
    test_path = os.path.join(os.path.expanduser("~"), "testing")
    os.rmdir(test_path)


@with_setup(setup_repo, teardown_repo)
def test_repo():
    test_path = os.path.join(os.path.expanduser("~"), "testing")
    assert ql.api.get_repo() == test_path
    assert os.path.isdir(ql.api.get_repo())
    assert ql.api.get_repo() == test_path


def test_list_scripts():
    assert isinstance(ql.api.list_scripts(), Iterable)
    assert isinstance(ql.api.get_scripts(), dict)
    assert len(ql.api.list_scripts()) == len(ql.api.get_scripts())


def test_list_commands():
    with mock.patch("quicklauncher.api.cmds", create=True):
        assert isinstance(ql.api.list_commands(), Iterable)
        assert isinstance(ql.api.get_commands(), dict)
        assert len(ql.api.list_commands()) == len(ql.api.get_commands())


def test_run_cmd():
    with mock.patch("quicklauncher.api.cmds", create=True):
        ql.api.run_cmd("ls")


def setup_script():
    setup_repo()
    with open(os.path.join(ql.api.get_repo(), "testsuite.py"), "w") as f:
        code = 'print("im in the root dir")'
        f.write(code)
    subdir = os.path.join(ql.api.get_repo(), "test")
    if not os.path.exists(subdir):
        os.mkdir(subdir)
    with open(os.path.join(subdir, "testsuite.py"), "w") as f:
        code = 'print("im in a subdir")'
        f.write(code)


def teardown_script():
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
    teardown_repo()


@with_setup(setup_script, teardown_script)
def test_run_script():
    ql.api.run_script("testsuite.py")
    ql.api.run_script("test/testsuite.py")
