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
    本文介绍的是windows版本的安装和使用

    一、所需下载准备的软件
    ghidra 9_1.2 （解压缩）
    jdk-11.0.7   （安装配置环境）
    
    ghidra 9_1.2 下载：
    链接：https://pan.baidu.com/s/1iLmW6HTbi4rCZJeW4M5xPw 
    提取码：lm1n
    
    jdk-11.0.7 下载：
    链接：https://pan.baidu.com/s/1kPapBPehOensCYyANfm3Yg 
    提取码：9ppd
    
    二、安装步骤
    
    1.下载ghidra源代码并压缩
    2.下载好后打开目录,双击ghidraRun.bat文件运行
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/01_ghidra%E8%BF%90%E8%A1%8C.png)
    
    3.如果出现这个界面的话就是配置成功
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/02_Ghidra%E8%BF%90%E8%A1%8C%E6%88%90%E5%8A%9F.png)

    4.如图所示,我们只需保留主程序窗口就可以了.
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/03_%E4%BD%BF%E7%94%A8%E6%AD%A5%E9%AA%A4.png)
    
    5.到此,我们就成功安装好了Ghidra,现在我们就可以使用它了.
    
    如何使用
    
        1.首先,我们来新建一个工程
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/04_%E5%88%9B%E5%BB%BA%E9%A1%B9%E7%9B%AE.png)
        
        2.我们选择个人项目,然后点击next
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/05_%E5%88%9B%E5%BB%BA%E4%B8%AA%E4%BA%BA%E9%A1%B9%E7%9B%AE.png)
        
        3.填写完之后点击finish
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/06_%E8%B7%AF%E5%BE%84%E8%AE%BE%E7%BD%AE.png)
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/07_0%E9%A1%B9%E7%9B%AE%E5%88%9B%E5%BB%BA%E5%A5%BD%E5%90%8E.png)
        
        4.导入需要分析的工具,或者直接将文件拖拽进工程
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/07_1%E5%AF%BC%E5%85%A5%E9%9C%80%E8%A6%81%E5%88%86%E6%9E%90%E7%9A%84%E9%A1%B9%E7%9B%AE.png)
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/07_2%E5%8A%A0%E8%BD%BD%E9%9C%80%E8%A6%81%E5%88%86%E6%9E%90%E7%9A%84%E6%96%87%E4%BB%B6.png)
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/07_3%E8%AE%BE%E7%BD%AE%E5%A5%BD%E5%90%8E%E7%82%B9OK.png)
        
        5.打开之后是这个界面,可以点击options设置
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/07_2_1%E8%AE%BE%E7%BD%AE%E9%80%89%E9%A1%B9.png)
        
        6.得到一个程序的信息
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/07_4%E4%BC%9A%E5%BC%B9%E5%87%BA%E5%88%86%E6%9E%90%E7%A8%8B%E5%BA%8F%E7%9A%84%E4%BF%A1%E6%81%AF.png)
        
        7.双击这个工程的exe程序,或者将程序拖入Tool Chest中小龙(Tool Chest可以自己添加工具)
   ![image](hhttps://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/08_%E5%8A%A0%E8%BD%BD%E9%9C%80%E8%A6%81%E5%88%86%E6%9E%90%E7%9A%84%E7%A8%8B%E5%BA%8F.png)
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/09_%E5%8F%8C%E5%87%BB%E5%8A%A0%E8%BD%BD%E7%A8%8B%E5%BA%8F.png)
        
        8.选择yes
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/07_5%E6%98%AF%E5%90%A6%E5%BC%80%E5%A7%8B%E5%88%86%E6%9E%90%E7%A8%8B%E5%BA%8F.png)
        
        
        9.按照默认的来,选择Analyze
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/07_6%E9%BB%98%E8%AE%A4%E8%AE%BE%E7%BD%AE%E5%B0%B1%E5%A5%BD.png)
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/10_%E5%8A%A0%E8%BD%BD%E7%94%BB%E9%9D%A2.png)
        
        10.等待一会,出现以下界面就打大功告成!
   ![image](https://github.com/kingking888/AndroidReverseEngineering/blob/master/Ghidra/src/png/13%E5%AE%8C%E6%88%90.png)
        
    

