---
title     : Visual Studio 的C语言支持很糟糕
tags      : c/c++, C#, python
mathjax   : true
published : true
toc       : true
---

Visual Studio 对于Ｃ++语言的支持应该说是很厉害的。但对于C语言的支持从来都是**能用，但不好用**。

编程的语言标准只是一个公约，各个平台上支持还得由具体的编译器或编程环境进行支持。也就是说，即使语言标准规定了某项内容，编译器或者编程环境也有可能不支持。

编程平台一般会将自己的C语言实现集成到一个标准库。只要链接这个标准库，程序员就可以使用库内的各种函数。在VS2015之前，每个版本的VS都会提供一份新的C语言运行时库，但是都是半成品

- 各个版本的运行时库之间互不兼容，所以很多程序报错会提示找不到MSCVRT.dll，msvcrt120.dll之类的问题
- 各个版本的运行时库对C语言标准的支持始终是**过时且残缺**的。

从VS2015开始，微软重构了Microsoft C 运行时库 (CRT)。 将标准 C 库、POSIX 扩展和 Microsoft 特定的函数、宏和全局变量移动到了新库，即通用 C 运行时库（通用 CRT 或 UCRT）。此后，只要是Window10+VS2015及更新版本，都可以使用。算是解决了之前CRT存在的问题，提高对标准的一致性。微软官方也极力推荐开发者将[将代码升级到通用 CRT](https://learn.microsoft.com/zh-cn/cpp/porting/upgrade-your-code-to-the-universal-crt?view=msvc-170)

但是**UCRT 支持基于 C 调用约定的稳定 ABI，且谨遵 ISO C99 标准（仅有少数例外）**。也就是说，**UCRT仅承诺支持1999年发布的C99标准**。怪不得SO上有人说它是上古时代的编译器，1980的过时编译器。

```text
Just don't use 1980s compilers like VS2022. It's the compiler that's broken and extremely outdated.

It's the stone age compiler that's broken. ISO C requires a diagnostic message here and has done so since 1999. 
```

## VS2022 骚操作导致的潜在bug实例。

`double difftime()` 是一个C语言的标准库`<time.h>`的函数，用来返回两个`time_t`型变量之间的时间间隔，即计算两个时刻之间的时间差。返回数值是一个`double`类型。

下面这段代码使用difftime()

```c
#include <stdio.h>

int main() {
    time_t t1, t2;
    t1 = 14;
    t2 = 0;
    printf("difftime =%f \n", difftime(t1, t2));
    return 0;
}
```
是一个可以在VS2022当中**成功编译，且不报错**的实例。
但是，这段代码在VS2022的显示结果是`difftime =0.00000`，而不是`difftime =14.00000`。

原因就在于，代码中没有正确引用对应的库函数`time.h`。因此在使用VScode+GCC编译，会直接报出一个错误来提示。

```
implicit declaration of function 'difftime' [-Wimplicit-function-declaration]
```

但是上述代码在VS2022中，却是可以**成功编译，且不报错**。**VS2022尽管知道`difftime()`在代码当中未定义，但它仅提供一个警告，且贴心地假设difftime返回值是int类型。** 而`int`类型又在`printf`行被悄悄地转换成了`double`类型，这段代码就这样制造了一个静悄悄的bug。

如果这段代码混在成百上千行代码的项目当中，就会是一个非常难以排查的问题。

## UCRT不支持 VLA
 
微软的UCRT还不支持可变数组，如下

```c
#include<stdio.h>

const int N = 10;

int main(void){
    int a[N];
    return 0；
}
```

此段代码在vs中为什么不能用，其他编译器却可以

「const int N」在C语言中并非编译期常量，且 VC不支持 C语言中 VLA ( Variable-Length Array )。

建议改 `const int N = 10;` 为`enum { N=10 };`

## 总结

1. 尽量避免使用VS编写C语言程序
2. 如果使用VS编写C程序，要注意所有的警告信息


程序员在编码过程中一定要**注意自己所使用的编程环境和所遵循的语言标准之间的匹配问题**。

## 参考链接

- [在vs中的c语言？ - 知乎](https://www.zhihu.com/question/663371165/answer/3585202465)
- [visual studio - difftime() return different data type in c on vs2022 - Stack Overflow](https://stackoverflow.com/questions/79341998/difftime-return-different-data-type-in-c-on-vs2022/79342033?noredirect=1#comment139914962_79342033)
- [difftime, _difftime32, _difftime64](https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/difftime-difftime32-difftime64?view=msvc-170)
- [C++入门基础知识136—【关于C 库函数 - difftime()】_c++ difftime-CSDN博客](https://blog.csdn.net/zhaoylzy/article/details/143492557)
