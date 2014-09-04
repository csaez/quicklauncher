QuickLauncher
=============
A quick menu to find and execute Maya commands and user scripts.


## Dependencies

- [PySide](http://qt-project.org/wiki/PySide)
- [Nose](http://nose.readthedocs.org) + [Coverage](http://coverage.readthedocs.org) + [Mock](http://mock.readthedocs.org) (testing)


## Installation

Copy/symlink `quicklauncher` directory somewhere in your `PYTHONPATH` (maya
scripts directory should do the trick) or clone the repo and install the
project through its `setup.py` script (_highly recommended!_).

    mayapy setup.py install


## Ussage

    import quicklauncher as ql
    
    # show menu
    ql.show()

    # repository dialog
    ql.select_repo()

    # ... or go deeper using the API
    ql.api.get_repo()
    ql.api.set_repo(repository_path)

    ql.api.get_scripts()  # {script_name: script_fullpath, ...}
    ql.api.list_scripts() # [script_name, ...]
    ql.api.run_script(script_name)
    
    ql.api.get_commands()  # {cmd_name: cmd_object, ...}
    ql.api.list_commands() # [cmd_name, ...]
    ql.api.run_cmd(cmd_name)


## Contributing

- [Check for open issues](https://github.com/csaez/quicklauncher/issues) or
open a fresh issue to start a discussion around a feature idea or a bug.
- Fork the [quicklauncher repository on Github](https://github.com/csaez/quicklauncher)
to start making your changes (make sure to isolate your changes in a local
branch when possible).
- Write a test which shows that the bug was fixed or that the feature works
as expected.
- Send a pull request and bug the maintainer until it gets merged and
published. :)

Make sure to add yourself to `CONTRIBUTORS.md`

## Limitations

- `quicklauncher` does not support MEL scripts at the moment.