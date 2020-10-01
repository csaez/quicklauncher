QuickLauncher
=============

A minimal Qt based menu to quickly find and execute Maya commands and user scripts.

![quicklauncher](https://cloud.githubusercontent.com/assets/2292742/20506707/8b19023c-b034-11e6-8598-a480924f8740.gif)


> `quicklauncher` relies on PySide/PySide2 and should work out of the box on Autodesk Maya 2014 or greater.


## Installation

There are many ways to go about this, but for casual users I would recommend to get the
[latest release](https://github.com/csaez/quicklauncher/releases) and simply copy
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

> **TIP:** You can refresh the list of available scripts without restarting Maya by simply
> reloading the python module in the script editor (or add a little python script that does
> this to your repo so it's available from the menu itself).
>
> ```python
> import quicklauncher
> reload(quicklauncher)
> ```

## Contributing

- [Check for open issues](https://github.com/csaez/quicklauncher/issues) or open a fresh issue to
  start a discussion around a feature idea or a bug.

- Fork the [quicklauncher repository on Github](https://github.com/csaez/quicklauncher) to start
  making your changes (make sure to isolate your changes in a local branch when possible).

- Write a test which shows that the bug was fixed or that the feature works as expected.

- Send a pull request and bug me until it gets merged. :)


Make sure to add yourself to `CONTRIBUTORS.md`!
