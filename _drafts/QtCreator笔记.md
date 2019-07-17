## 在已经打开的文件中切换

Ctrl+Tab 

## 程序一开始执行就出现 The inferior stopped because if received a signal from the operating system.

如下图所示

![](./pic/1490533009.png)

但是我确定程序没有问题，所以一定是某些设置出现问题；而且这个bug是在程序进入主函
数之前弹出的，因此也无法调试。

But I am sure that my program is ok, so it will be wrong at my settings. This
popup window turns out before my program enters its main function. so I can not
debug it by code.

这个据我推测是一个qt的bug，解决办法是取消项目设置中的run in terminal，使用自带
的Application Output查看变量输出情况。

I think this is a bug of qtcreator, I have to cancel "run in terminal" in
"project"

![](./pic/1490533253.png))

Qt is good, but not good enough, yet.

# 如何在qt工程中区分debug和release模式

Literally, this works:

```makefile
CONFIG(release, debug|release) {
    message(Release)
    DEFINES += A B
}

CONFIG(debug, debug|release) {
    message(Debug)
    DEFINES += A
}
```

While this does not:

```makefile
CONFIG(release, debug|release) 
{
    message(Release)
}

CONFIG(debug, debug|release) 
{
    message(Debug)
}
```

也就是说要把括号的位置放对。我测试了一下(2017年07月14日17:40:33
QtCreator4.2.0, debian testing)，第二种方法在程序编译后，也已经是有效的。但是第
一种方法更好。

1. 使用第一种方法，从debug切换至release模式，如下所示代码会直接变灰，表示不可用
   。编译程序运行后，也不会打印那一行。

```c
#ifdef B
    printf("B is defined!\n");
#endif
```

2. 使用第二种方法，从debug切换至release模式，上面所示代码会不会变灰，表示不可用
   。但编译程序运行后，也不会打印那一行。

[原文链接](https://stackoverflow.com/questions/19562591/qt-creator-config-debug-release-switches-does-not-work)

## qtcreator设置C和C++语言编译参数

有时为了便于编译，需要对gcc的编译参数进行设置，当你的项目是C语言程序时，应当在
.pro文件中添加

```makefile
QMAKE_CFLAGS += -Wno-unused-but-set-variable #你的参数
```

当你的项目是C++语言程序时，应当在.pro文件中添加

```makefile
QMAKE_CXXFLAGS += -Wno-unused-but-set-variable #你的参数
```

## Qt Creator: During startup program exited with code

一般是因为引用了dll，但是可执行程序无法找到该dll

解决办法：把dll复制进去就行了。

## 无法启动此程序因为计算机中丢失*.dll

比如说WIN7系统-开始-计算机-右键-属性-高级系统设置，高级选项卡-环境变量-系统变量
，

添加如下路径：

D:\Qt\Qt5.5.1\Tools\mingw492_32\bin;

D:\Qt\Qt5.5.1\Tools\QtCreator\bin\

# QtCreator打开文件时间过长 

- Remove Creator's settings from %APPDATA%.
- Start Creator.
- Make sure that Creator automatically detected a Qt 5 kit. If not, add one in "Tools" -> "Options...".
- Have a clean checkout of Qt 4.8.5's sources.
- Open projects.pro from this repository.
- It will take nearly three minutes until Creator switches to Projects mode and
 shows the "Configure Project" screen. Most of the time Creator's memory
 consumption does not rise and the CPU is idle.

![Opening pro files takes too long](https://bugreports.qt.io/browse/QTCREATORBUG-10733)

# no-qmlscene-installed qmlscene未安装

解决办法

```bash
sudo apt-get install qtdeclarative5-dev
```

# 安装XML包时显示cannt find xml2-config

```bash
sudo apt-get install libxml2-dev libxml2
```

