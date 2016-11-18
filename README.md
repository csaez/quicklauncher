QuickLauncher
=============

A minimal Qt based menu to quickly find and execute Maya commands and user scripts.

![quicklauncher](https://cloud.githubusercontent.com/assets/2292742/17669950/1be0ea84-6353-11e6-8726-f233cfc2ea25.gif)

> `quicklauncher` relies on PySide/PySide2 and should work out of the box on Autodesk Maya 2014 or greater.


## Installation

There are many ways to go about this, but for casual users I would recommend simply copy
`quicklauncher.py` to your maya script directory.

If you are a developer or want to integrate quicklauncher in your pipeline, I highly recommend
the standard `setup.py` script as it brings more flexibility.

```python
python setup.py install
```


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

For more info, check the [Wiki][] (there are a few interesting things you can do).

[Wiki]: https://github.com/csaez/quicklauncher/wiki


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
