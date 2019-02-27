# Jays-PyCOM
A tiny serial port assistant (GUI) based on Python2.7+wxPython4.0+pySerial | 一款超轻量级的串口调试助手  

[![GitHub release](https://img.shields.io/github/release/JayHeng/Jays-PyCOM.svg)](https://github.com/JayHeng/Jays-PyCOM/releases/latest) [![GitHub commits](https://img.shields.io/github/commits-since/JayHeng/Jays-PyCOM/v1.0.0.svg)](https://github.com/JayHeng/Jays-PyCOM/compare/v1.0.0...master) [![GitHub license](https://img.shields.io/github/license/JayHeng/Jays-PyCOM.svg)](https://github.com/JayHeng/Jays-PyCOM/blob/master/LICENSE.txt)

English | [中文](./README.md)

<img src="http://henjay724.com/image/cnblogs/JaysPyCOM_v1.0.0_overview.png" style="zoom:100%" />

### 1. How to use :
********************
　　Jays-PyCOM.exe is green software, you don't need to install it, just open it directly under "\Jays-PyCOM\bin\" dictionary

> Note: The Jays-PyCOM.exe in the source code package is packaged in the Windows 10 x32 environment and has only been tested in this environment. If it cannot be used directly for system environment reasons, you need to rebuild it.  

### 2. How to rebuild :
********************
　　First of all, , you need to install all Non-Python packages listed in [《Jays-PyCOM环境搭建》](http://www.cnblogs.com/henjay724/p/9416049.html), then follow below steps:  
```text
  1. Install Python2.7.15 x86 version
  2. Confirm that the directory "\Python27\" and "\Python27\Scripts\" are in the system environment variable path after the installation is completed
  3. Double click "\Jays-PyCOM\env\do_setup_by_pip.bat" to install the Python library on which Jays-PyCOM depends
  4. Double click "\Jays-PyCOM\env\do_pack_by_pyinstaller.bat" to regenerate the Jays-PyCOM.exe
  5. Open "\Jays-PyCOM\bin\Jays-PyCOM.exe" to use it
```

### 3. Tool Features :
********************
* Auto-detect all available COM Ports  
* Both receive and send are supported  
* View data in Hex or Text(ASCII) format  
* Show statistics and error information  
* Design detail: [《Jays-PyCOM诞生记(全六篇)》](https://www.cnblogs.com/henjay724/p/9416096.html)

### 4. License :
********************
　　This package is licensed under the BSD three-clause license. See the LICENSE.txt file for details.

Copyright © 2017-2018 Jay Heng.