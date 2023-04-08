=== IconFinder

== Purpose
This package is a simple tool intended to easily, given the path for some executable in any of the "Big Three" most used OSes, provide the path to the icon for that executable.

== Usage
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
