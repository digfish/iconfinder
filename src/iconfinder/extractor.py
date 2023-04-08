import sys,os

import PIL.Image

if sys.platform == 'win32':
    import win32api
    import win32gui
    import win32con
    import win32ui


class Extractor:

    def __init__(self, icon_path):
        self.icon_path = icon_path

    def extract(self):
        if sys.platform == "win32":
            return self._extract_from_exe()
        else:
            return self._extract()

    def _extract(self):
        if os.path.exists(self.icon_path):
            return PIL.Image.open(self.icon_path)
        return None


    def _extract_from_exe(self):
        '''
        Returns the icon of the executable as a PIL Image Object
        :param exe_path: the path of the .exe
        :return: a PIL Image Object
        '''
        large, small = win32gui.ExtractIconEx(self.icon_path, 0)
        win32gui.DestroyIcon(large[0])
        ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
        #creating a destination memory DC
        hdc = win32ui.CreateDCFromHandle( win32gui.GetDC(0) )
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, ico_x, ico_x)
        hdc = hdc.CreateCompatibleDC()
        hdc.SelectObject(hbmp)
        #draw a icon in it
        hdc.DrawIcon( (0,0), small[0] )
        win32gui.DestroyIcon(small[0])
        #convert picture
        hbmp.GetBitmapBits(True)
        im = PIL.Image.frombuffer("RGBA", (ico_x,ico_x), hbmp.GetBitmapBits(True), "raw", "BGRA", 0, 1)
        #im = im.resize((16,16),PIL.Image.LANCZOS)
        return im

def main():
    if len(sys.argv) > 1:
        extractor = Extractor(sys.argv[1])
        print(extractor.extract())
    else:
        if sys.platform == 'win32':
            extractor = Extractor("C:\\windows\\explorer.exe")
            print(extractor.extract())
        elif sys.platform == 'linux':
            extractor = Extractor("xeyes")
            print(extractor.extract())
        elif sys.platform == 'darwin':
            extractor = Extractor("/System/Library/CoreServices/Finder.app")
            print(extractor.extract())

if __name__ == "__main__":
    main()
