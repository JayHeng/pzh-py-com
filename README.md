# 痞子衡串口调试助手
A tiny serial port assistant (GUI) based on Python2.7+wxPython4.0+pySerial | 一款超轻量级的串口调试助手  

[![GitHub release](https://img.shields.io/github/release/JayHeng/pzh-py-com.svg)](https://github.com/JayHeng/pzh-py-com/releases/latest) [![GitHub commits](https://img.shields.io/github/commits-since/JayHeng/pzh-py-com/v1.0.0.svg)](https://github.com/JayHeng/pzh-py-com/compare/v1.0.0...master) [![GitHub license](https://img.shields.io/github/license/JayHeng/pzh-py-com.svg)](https://github.com/JayHeng/pzh-py-com/blob/master/LICENSE.txt)

[English](./README-en.md) | 中文

<img src="http://henjay724.com/image/cnblogs/JaysPyCOM_v1.0.0_overview.png" style="zoom:100%" />

### 1. 安装与使用:
********************
　　痞子衡串口调试助手是纯绿色软件，不需要安装，直接在"\pzh-py-com\bin\"目录下双击打开即可。  

> 注意: 痞子衡串口调试助手是在Windows 10 x32环境下打包的，也仅在该环境下测试过。如果痞子衡串口调试助手下载后不能在你的当前系统环境下运行，你需要自己重新打包。  

### 2. 二次开发及重编:
********************
　　参考这篇文章 [《痞子衡串口调试助手-开发环境搭建》](http://www.cnblogs.com/henjay724/p/9416049.html) 安装所有非Python相关的开发工具, 然后按照如下步骤继续安装Python环境:  
```text
  1. 安装Python2.7.15 x86 version  
  2. 确认系统路径包含"\Python27\" 和 "\Python27\Scripts\"  
  3. 双击"\pzh-py-com\env\do_setup_by_pip.bat"脚本安装所有依赖的第三方Python库  
  4. 双击"\pzh-py-com\env\do_pack_by_pyinstaller.bat"脚本重新生成pzh-com.exe  
  5. 双击"\pzh-py-com\bin\pzh-com.exe"运行  
```

### 3. 软件功能:
********************
* 支持自动检测当前PC上的所有可用COM端口  
* 支持串口数据收发  
* 支持串口数据以两种格式(Hex/Ascii)显示  
* 支持串口数据收发统计与错误提示（在状态栏）  
* 软件设计细节详见: [《痞子衡串口调试助手诞生记(全六篇)》](https://www.cnblogs.com/henjay724/p/9416096.html)  

### 4. 许可证:
********************
　　软件采用BSD three-clause license， 更多许可证细节详见LICENSE.txt.  

Copyright © 2017-2018 Jay Heng.