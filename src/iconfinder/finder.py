import os
import sys
if 'extractor' not in sys.modules:
    from . import extractor

if sys.platform == 'linux':
    import xdg.IconTheme
    from xdg.IconTheme import getIconPath
elif sys.platform == 'darwin':
    import plistlib

class Finder:
    def __init__(self, executable):
        self.executable = executable
        self.icon_filepath = self.find()

    def find(self):
        print("Finding icon for: " + self.executable + "")
        if sys.platform == "win32":
            return self.executable if os.path.exists(self.executable) else None
        elif sys.platform == 'linux':
            return self._find_from_xdg()
        elif sys.platform == 'darwin':
            return self._find_from_plist()

    def _find_from_plist(self):
        '''
        Returns a PIL Image referencing a ICNS icon file
        '''
        plist_path = self.executable + '/Contents/Info.plist'
        if os.path.exists(plist_path):
            plistdict = plistlib.load(open(plist_path, 'rb'))
            if 'CFBundleIconFile' in plistdict:
                icon_name = plistdict['CFBundleIconFile']
                icon_filepath = self.executable + '/Contents/Resources/' + icon_name + '.icns'
                if os.path.exists(icon_filepath):
                    return icon_filepath
        return None

    def _find_from_xdg(self):
        '''
        Returns the path of the icon as discovered by XDG
        :return: the icon file path
        '''
        icon_path = getIconPath(os.path.basename(self.executable),size=32)
        return icon_path if icon_path else None

    def grab(self):
        '''
        Returns a PIL Image Object referencing the icon 
        '''
        return extractor.Extractor(self.icon_filepath).extract()




def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            if sys.platform == 'win32':
                finder = Finder("C:\\windows\\explorer.exe")
            elif sys.platform == 'linux':
                finder = Finder("/usr/bin/leafpad")
            elif sys.platform == 'darwin':
                finder = Finder("/System/Library/CoreServices/Finder.app")
        else:
            finder = Finder(sys.argv[1])
        print(finder.icon_filepath)
        print(finder.grab())
    else:
        print("You need to specify 'test' or specify the path for an executable")


if __name__ == "__main__":
    main()
        