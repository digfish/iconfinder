import sys
import os
sys.path.append('./src')
import iconfinder.finder as finder
import PIL.Image


def test_find():
    # Test if the function returns expected output
    if sys.platform == 'win32':
        assert finder.Finder('c:\\windows\\explorer.exe').find() == 'c:\\windows\\explorer.exe'
    elif sys.platform == 'darwin':
        assert finder.Finder('/System/Library/CoreServices/Finder.app').find() == '/System/Library/CoreServices/Finder.app/Contents/Resources/Finder.icns'
    elif sys.platform == 'linux':
        assert finder.Finder('/usr/bin/leafpad').find() == '/usr/share/icons/hicolor/32x32/apps/leafpad.png'

    # Test for error handling
    # with pytest.raises(ValueError):
    #     my_module.my_function(0, 5)

def test_grab():
    if sys.platform == 'win32':
        _finder = finder.Finder('c:\\windows\\explorer.exe')
        im = _finder.grab()
        print(im)
        assert type(im) == PIL.Image.Image
    elif sys.platform == 'darwin':
        _finder = finder.Finder('/System/Library/CoreServices/Finder.app')
        im = _finder.grab()
        print(im)
        assert type(im) == PIL.IcnsImagePlugin.IcnsImageFile
    elif sys.platform == 'linux':
        _finder = finder.Finder('/usr/bin/leafpad')
        im = _finder.grab()
        print(im)
        assert type(im) == PIL.PngImagePlugin.PngImageFile
        #assert type(im) == PIL.Image.Image

