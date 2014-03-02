QuickLauncher
=============
A quick menu to find and execute Softimage/Maya commands and scripts.

![](docs/quicklauncher.gif?raw=true)

Dependencies
------------
- [wishlib](http://github.com/csaez/wishlib)
- [PyQtForSoftimage](http://github.com/caron/PyQtForSoftimage) (Softimage)

Installation
------------
###Softimage version:
- Grab a pre-packed xsiaddon from [here](http://goo.gl/e2WWN7) and drop
it on a softimage viewport.

*or...*

- Install the python modules and copy/symlink `quicklauncher_plugin.py` to
a softimage plugin directory.

###Maya version:
- Grab a pre-packed zip from [here](http://goo.gl/yEm4V1) and uncompress the
contents in your user script directory.

*or...*

- Install the python modules.

### Python modules:
Clone the repo and type in a terminal:

    python setup.py install


Ussage
------
    import quicklauncher
    quicklauncher.show()    # launch the menu
    quicklauncher.prefs()   # preferences
    quicklauncher.reload()  # update the command/plugin list

> Note: Softimage version include custom commands for launch, prefs and
> reload!

For further information refer to the [documentation](https://github.com/csaez/quicklauncher/wiki).
