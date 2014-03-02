QuickLauncher
=============
A quick menu to find and execute Softimage/Maya commands and scripts.

![](quicklauncher.gif?raw=true)

Dependencies
------------
- [wishlib](http://github.com/csaez/wishlib)
- [PyQtForSoftimage](http://github.com/caron/PyQtForSoftimage) (Softimage)

Installation
------------
###Softimage version:
*The easy way*: Grab a pre-packed xsiaddon from [here](http://goo.gl/e2WWN7)
(includes wishlib) and drop it on a softimage viewport.

*The 'hard' way*: Install the python modules and copy/symlink
`quicklauncher_plugin.py` to a softimage plugin directory.

###Maya version:
Install the python modules and copy/symlink `quicklauncher.py` to your script
directory (or use the source code directly).

### Python modules:
Clone the repo and type in a terminal:

    python setup.py install


Ussage
------
Refer to the [documentation](https://github.com/csaez/quicklauncher/wiki).
