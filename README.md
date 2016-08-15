QuickLauncher
=============

A minimal Qt based menu to quickly find and execute Maya commands and user scripts.

![quicklauncher](https://cloud.githubusercontent.com/assets/2292742/17669950/1be0ea84-6353-11e6-8726-f233cfc2ea25.gif)

> `quicklauncher` relies on PySide, it should work out of the box on Autodesk Maya 2014 or greater.


## Installation

Append inner `quicklauncher` directory to your PYTHONPATH.

- **Windows**
```bat
$ cd quicklauncher
$ set PYTHONPATH=%PYTHONPATH%;%CD%\quicklauncher
```

- **Unix**
```bash
$ cd quicklauncher
$ export PYTHONPATH=${PYTHONPATH}:${PWD}/quicklauncher
```

Or use the standard `setup.py` script.


## Usage

```python
import quicklauncher
quicklauncher.show()
```

You can also select the folder in which `quicklauncher` will look for user scripts (repo).

```python
import quicklauncher
quicklauncher.select_repo()
```

And alternatively, assign TAB key.

```python
import quicklauncher
quicklauncher.setup_hotkey()
```

> Be aware that the later override Maya default behavior of the tab key jumping between inputs in the
> attribute editor and editors alike.


For more info (there are a few interesting things you can do), check the [Wiki][]

[Wiki]: https://github.com/csaez/quicklauncher/wiki


## Running tests

This is not something the average user should worry about, but if you want to contribute to `quicklauncher` development you can run the test suite by typing the following from the root of the project.

```bash
python setup.py test
```

> Testing requires `mock`, it should be automatically installed by running the previous snippet in case it's not already available on your system.


## Contributing

- [Check for open issues](https://github.com/csaez/quicklauncher/issues) or open a fresh issue to
  start a discussion around a feature idea or a bug.

- Fork the [quicklauncher repository on Github](https://github.com/csaez/quicklauncher) to start
  making your changes (make sure to isolate your changes in a local branch when possible).

- Write a test which shows that the bug was fixed or that the feature works as expected.

- Send a pull request and bug me until it gets merged. :)


Make sure to add yourself to `CONTRIBUTORS.md`!


## Known issues

- `quicklauncher` does not supports MEL scripts at the moment.
