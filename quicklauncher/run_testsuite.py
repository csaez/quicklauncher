import os
import sys

try:
    import mock
    import nose
except ImportError:
    print "Test-suite requires mock and nose libraries"

# Mock host-dependent modules, as they aren't available
# outside of Maya.
sys.modules['maya'] = mock.Mock()
sys.modules['shiboken'] = mock.Mock()

# Expose package to PYTHONPATH
path = os.path.dirname(__file__)
sys.path.insert(0, path)


if __name__ == '__main__':
    argv = sys.argv[:]
    argv.extend(['--verbose'])
    nose.main(argv=argv)
