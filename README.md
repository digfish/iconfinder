# IconFinder

## Purpose
This package is a simple tool intended to easily, given the path for some executable in any of the "Big Three" most used OSes, provide the path to the icon for that executable.

For example, you can use it to fill a list view for a launcher with the icons from the applications you wish to execute.

## Usage
There are two modules in this package. One is 'finder' with Finder class, which, through the constructor `iconfinder.Finder('path/to/some/executable')` will return the path to the executable `icon_filepath`. The other is 'extractor' which has the Extractor class, which, through the constructor `iconfinder.Extractor('path/to/an/icon')` will return the icon as a PIL Image object `icon_image`.
If you use Finder to get the icon path, you can simply use the method `grab` from the finder instance.
For example, under Windows:

```python
>>> from iconfinder import finder
>>> finder_instance = finder.Finder('C:\\Windows\\System32\\notepad.exe')
>>> finder_instance.icon_filepath # this is the path to the icon
>>> finder_instance.grab() # this is the icon as a PIL Image object
```

**Note**: on Windows is not necessary to use first class Finder since the icon comes inside the binary. 

## Dependencies
This library is dependent, under Windows, of the [pywin32](https://pypi.org/project/pywin32/) package. Under Linux, uses [pyxdg](https://freedesktop.org/wiki/Software/pyxdg/), and under the mac, the [plistlib](https://docs.python.org/3/library/plistlib.html), which cames pre-packaged with the Python Standard Library.
Of course, [Pillow](https://python-pillow.org/) is also a dependency.

## Testing from command line
To run the unit tests, clone the repo and execute `pytest` from the main directory.
To get a taste of the library, you can run `python -m iconfinder.finder` or just `iconfinder` with the executable path from the main directory. Specifying `test` as the argument will perform a test with a default executable and quit.
