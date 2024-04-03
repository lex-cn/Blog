---
tags: Linux
toc : true
---

# gdb命令行选项

```bash
gdb -x filename  # 从脚本启动
```

# gdb内的操作

```gdb
show args  # 显示输入的变量
until      # 跳出循环
list       # 显示10行代码
list n     # 显示第n行前后10行的代码
```

# optimized out

gdb调试查看变量的值的时候,出现`<optimized out>`错误

解决方法是将:

- -O3 或者其他的数字修改为0
- -O0  意思是不进行优化

# 如何查看数组指针内的值

```c
int a[5] = {1,2,3,4,5};
int *p = a;
```

gdb查看p的子元素数值

```bash
p *p@5
```

# gdb 调试


## windwos下使用gcc链接libmysql

gcc从4.6版本开始，已经可以直接链接.dll文件，不需要别的软件进行转化。

## 每次都重新编译整个工程

最近重装了系统，每次编译工程都要重新编译，非常慢，但是又找不出问题。

几经搜索，在下面这篇文章中找到了结果文件。

[出错总有原因之工程每次都重新编译
](http://blog.csdn.net/cisse/article/details/18996245)

每次重新编译的原因，是因为装完系统之后，我的系统时间提前了几天，在这期间我复制
了这个文件。我发现后，改系统时间，但是头文件的时间戳还是提前的，这就让编译器每
次重新编译这些文件。


## Cannot access memory at address

这个错误的来源一般是**越界访问，溢出，段错误**

> 在占用内存空间较大的局部数组声明的前面加static将其从堆栈数据段挪到全局数据段即可。
> 堆栈大小默认1MB
> 可以在链接选项中改大。

如果这个错误在函数的调用处发生，一般可以确定是堆栈溢出，因此要注意这个函数的输
入变量的大小，尽量减小输入参数的数量或这结构体大小

如果其他情况，那么是数组等变量越界访问，要注意数组访问时的下标是否过大。

参考连接:
[CSDN问答](https://bbs.csdn.net/topics/390444341)

## gdb如何打印宏定义

在CFLAGS参数后添加-g3 参数 , 不需要-gdwarf-2参数

> 原来-g参数也是带等级的, :)

参考链接:[https://blog.csdn.net/zhangjs0322/article/details/39666889](https://blog.csdn.net/zhangjs0322/article/details/39666889)


## gdb 命令缩写
```Bash
info i
breakpoints bre
```

## make

make似乎会自动判定目标文件是否存在及其最新的时间，以此来判定make是否已经完成，而不是文件的内容。

