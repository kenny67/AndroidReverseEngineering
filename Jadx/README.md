# Jadx

Jadx简介

    Android开发人员的日常工作中免不了要向其它优秀App学习借鉴。
    俗话说：“工欲善其事，必先利其器”，下面介绍一下常用的逆向工具。
    jadx是个人比较喜欢的一款反编译利器，同时支持命令行和图形界面，
    能以最简便的方式完成apk的反编译操作。
    先给出工具的GitHub地址，可以按照自己喜欢的方式安装并查看功能文档：
    
    源码地址：https://github.com/skylot/jadx
    

## Usage
    1.下载
    https://bintray.com/skylot/jadx/releases/v1.1.0#files/
    
    2.以管理员身份运行
    
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Jadx/src/png/01运行.png)
    
    3.加载需要分析的app
    
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Jadx/src/png/02选择需要分析的APK.png)
    
    4.app的整体结构
    
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Jadx/src/png/03APP源文件结构和代码.png)
    
    5.查找关键函数
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Jadx/src/png/04查找关键字.png)
   
    
    6.分析源代码
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Jadx/src/png/05success.png)
    
##Problem
    如何修改jadx的默认内存
    1.使用记事本或者notpad++打开jadx-gui.bat。
    2.找到 set DEFAULT_JVM_OPTS="-Xms128M" "-Xmx4g" 。
    3.将其修改为 set DEFAULT_JVM_OPTS="-Xms128M" "-Xmx8g" 后保存就ok了。
    


