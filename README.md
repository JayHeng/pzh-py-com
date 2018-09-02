# JaysPyCOM
A tiny serial port assistant based on pySerial + wxPython

<img src="http://odox9r8vg.bkt.clouddn.com/image/cnblogs/JaysPyCOM_overview.png" style="zoom:100%" />

### How to use :
********************
JaysPyCOM.exe is a free application, you don't need to install it, just open it directly under "\JaysPyCOM\bin\" dictionary
> Note: it is only verified in environment: Windows 10, x64bit, if you cannot use it, please try to build it by yourself

### How to build :
********************
First of all, you should install all packages listed in [《JaysPyCOM环境搭建》](http://www.cnblogs.com/henjay724/p/9416049.html), then follow below steps:
```text
  1. cd to "\JaysPyCOM\bin\"
  2. Update pathex in JaysPyCOM.spec to current path in your PC
  3. run "pyinstaller JaysPyCOM.spec"
  4. You will see "\JaysPyCOM\bin\dist\JaysPyCOM.exe" is generated
  5. Move JaysPyCOM.exe to dictionary "\JaysPyCOM\bin\" (this step is a MUST!!!)
  6. Open "\JaysPyCOM\bin\JaysPyCOM.exe" to use it
```

### Features in v1.0.0 :
********************
* Auto-detect all available COM Ports
* Both receive and send are supported
* View data in Hex or Text(ASCII) format
* Show statistics and error information
* Design detail: [《JaysPyCOM诞生记(全六篇)》](https://www.cnblogs.com/henjay724/p/9416096.html)

### License :
********************
This package is licensed under the BSD three-clause license. See the LICENSE.txt file for details.

Copyright © 2017-2018 Jay Heng.