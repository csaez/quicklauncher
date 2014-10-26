QuickLauncher
=============
A quick menu to find and execute Maya commands and user scripts.

#### Installation

> Requires Autodesk Maya 2014+

Append inner `quicklauncher` directory to PYTHONPATH.

- **Windows**

 ```bat
$ cd quicklauncher
$ set PYTHONPATH=%PYTHONPATH%;%CD%\quicklauncher
```

- **Unix**

 ```bash
# Unix
$ cd quicklauncher
$ export PYTHONPATH=${PYTHONPATH}:${PWD}/quicklauncher
```

## Usage

```python
import quicklauncher
quicklauncher.show()
```

Alternatively, assign TAB key.

```python
import quicklauncher
quicklauncher.setup_hotkey()
```

Then press TAB.

For more info, check the [Wiki][]

[Wiki]: https://github.com/mottosso/quicklauncher/wiki

#### Contributing

- [Check for open issues](https://github.com/csaez/quicklauncher/issues) or open a fresh issue to start a discussion around a feature idea or a bug.
- Fork the [quicklauncher repository on Github](https://github.com/csaez/quicklauncher) to start making your changes (make sure to isolate your changes in a local branch when possible).
- Write a test which shows that the bug was fixed or that the feature works as expected.
- Send a pull request and bug the maintainer until it gets merged and
published. :)

Make sure to add yourself to `CONTRIBUTORS.md`

#### Limitations

- `quicklauncher` does not support MEL scripts at the moment.
