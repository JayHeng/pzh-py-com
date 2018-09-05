import wx
from wx.tools.img2py import img2py
import sys, os

class myImg2py(object):

    def __init__(self):
        pass

    def start(self):
        imgFolderPath =  os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'img')
        fileLists = os.listdir(imgFolderPath)
        for file in fileLists:
            fileName = os.path.splitext(file)[0]
            fileFormat = os.path.splitext(file)[1]
            imgFilePath = os.path.abspath(os.path.join(imgFolderPath, file))
            if (fileFormat == '.png') or (fileFormat == '.jpg') or (fileFormat == '.ico') or (fileFormat == '.bmp') or (fileFormat == '.gif'):
                # Don't convert image file named tinypycom.png
                if (file != 'tinypycom.png'):
                    pyFilePath = os.path.abspath(os.path.join(imgFolderPath, fileName + '.py'))
                    img2py(imgFilePath, pyFilePath)
            else:
                print("Unrecognized file: %s\n" %(imgFilePath))

if __name__ == '__main__':
    myImg2py().start()

