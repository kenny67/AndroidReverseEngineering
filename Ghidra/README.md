# Ghidra

    Ghidra是由美国国家安全局（NSA）研究部门开发的软件逆向工程（SRE）套件，
    是一个软件逆向工程（SRE）框架，包括一套功能齐全的高端软件分析工具，
    使用户能够在各种平台上分析编译后的代码，包括Windows、Mac OS和Linux。
    功能包括反汇编，汇编，反编译，绘图和脚本，以及数百个其他功能。
    Ghidra支持各种处理器指令集和可执行格式，可以在用户交互模式和自动模式下运行。
    用户还可以使用公开的API开发自己的Ghidra插件和脚本。

    开源地址：https://github.com/NationalSecurityAgency/ghidra
    下载地址：https://www.ghidra-sre.org/ （注意：需要很高的梯子）

## Usage

    一、所需下载准备的软件
    ghidra 9_1.2
    jdk-11.0.7
    (如果觉得麻烦可以去我的主页直接下载)
    
    二、安装步骤
    
    1.下载ghidra源代码并压缩
    2.下载好后打开目录,双击ghidraRun.bat文件运行
    ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/01_ghidra%E8%BF%90%E8%A1%8C.png)
    
    3.如果出现这个界面的话就是配置成功
    ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/02_Ghidra%E8%BF%90%E8%A1%8C%E6%88%90%E5%8A%9F.png)

    4.如图所示,我们只需保留主程序窗口就可以了.
    ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/03_使用步骤.png)
    
    5.到此,我们就成功安装好了Ghidra,现在我们就可以使用它了.
    
    如何使用
    
        1.首先,我们来新建一个工程
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/04_创建项目.png)
        
        2.我们选择个人项目,然后点击next
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/05_创建个人项目.png)
        
        3.填写完之后点击finish
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/06_路径设置.png)
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/07_0项目创建好后.png)
        
        4.导入需要分析的工具,或者直接将文件拖拽进工程
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/07_1导入需要分析的项目.png)
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/07_2加载需要分析的文件.png)
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/07_3设置好后点OK.png)
        
        5.打开之后是这个界面,可以点击options选择添加外部库
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/07_3设置好后点OK.png)
        
        6.得到一个程序的信息
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/07_4会弹出分析程序的信息.png)
        
        7.双击这个工程的exe程序,或者将程序拖入Tool Chest中小龙(Tool Chest可以自己添加工具)
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/08_加载需要分析的程序.png)
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/09_双击加载程序.png)
        
        8.选择yes
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/07_5是否开始分析程序.png)
        
        
        9.按照默认的来,选择Analyze
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/07_6默认设置就好.png)
        
        10.等待一会,出现以下界面就打大功告成!
        ![image](https://github.com/kingking888/AndroidReverseEngineering/tree/master/Ghidra/src/png/11_加载成功画面.png)
        
    

