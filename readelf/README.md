# AndroidReverseEngineering

安卓逆向工程之so文件分析

    SO文件是Linux下共享库文件，它的文件格式被称为ELF文件格式。在Android逆向中对so文件格式分析非常重要。
    ELF文件主要由 ELF header 、section header table、program header table组成

    ELF header

        什么是ELFheader？

        所谓的elfHeader也就是系统要解析一个elf文件第一步需要解析的地方，怎么解析不是本章的主要，本章只分析elf文件整体的框架，方面在脑袋里形成图画。所以elf文件头部包含了整个elf文件重要组成部分的offset，什么是重要的组成部分？上面说到了section header table、program header table。

    ELFheader的组成:  
    
        1.固定格式（ident/type/machine/version/entry）:这些成员在同类型的elf文件中一般是固定的
    
        2.sectionHeaderTable信息（shoff/shentsize/shnum）:此三个成员描述的是sectionHeaderTable的偏移、单个大小、总个数
    
        3.programHeaderTable信息（phoff/phentsize/phnum）：同上，描述的是programHeaderTable的信息
    
        4.字符串表在sectionHeaderTable中的位置（这个先不说了，说也说不明白，等第二篇解析ELF文件的时候在说，总之有这个东西）
    
        换句话说：通过elfHeader我们便可获取到elf文件的各种信息。因为已经获取到了其他两个table的偏移、单个大小、总个数

    section header table
    
     什么是section header table？
    
        一句话：一个so里面所有的资源。如变量名、字符串、执行代码、got、plt等。。。
    
    sectionHeaderTable的组成：
    
        1.由多个sectionHeader组成，至于是多少个？上面ELFHreader已经告诉我们了
    
        2.每个sectionHeader又代表了不同的资源。如上面说的变量名、字符串、执行代码等。。。
    
        换句话说：section header table表示so里面所有的资源的一个表单
    
    program header table

    什么是program header table？
    服务于sectionHreader的一张表!
    
     sectionHeaderTable的组成：
    
        1.一个sectionHeaderTable由多个segment组成.
    
        2.而一个segment包含多个section
    
    换句话说: 从组成结构上可以看得出他主要是服务于section的,而section又是so的资源,所以狭义上我们可以理解成此表为告诉计算机要怎么加载解析so资源的一张表.
     
使用:

    Run readelf 
    然后输入so的路径


