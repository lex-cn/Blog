---
title  : unsigned char 和uint8_t的区别
tags   : C语言
categories : 
excerpt: 此处写摘要
mathjax: true
published  : true 
toc    : true
---


今天发现有些代码当中使用`uint8_t`代替`unsigned char`来对数据进行声明。

大致进行搜索了一下，基本内容如下


1. char的字节长度不是固定的，虽然大部分系统的实现都是8个字节，但可能会有例外

    char的大小是：exactly one byte in size, at least 8bits。

    `uint8_t`才是真正的8bit

2. 因为在大部分系统中，两者的效果基本上一致。 如果没有实现uint8_t的系统中，可以由`typedef`重新定义。

    ```c
    typedef unsigned char uint8_t;
    typedef unsigned short int uint16_t;
    ```

3. C99标准规定，在stdint.h中定义的`uint8_t`是绝对的8bit；在对内存要求严格的环境中，这点非常重要。 

    ```c
    unsigned short   uint8_t 
    signed char      int8_t 
    unsigned short   uint16_t
    short            int16_t 
    unsigned int     uint32_t
    int              int32_t
    ```

4. 此外，`uint8_t`能够更清楚地表明，我们定义的是一个取值范围更短的数字，而非什么char。

    > It documents your intent - you will be storing small numbers, rather than a character.

综上所述，在能采用C99标准的环境里，`uint8_t`系列的选择显然更好。

参考资料

- [Difference between char, signed char, unsigned char, uint8_t, int8_t and std::byte? : cpp_questions](https://www.reddit.com/r/cpp_questions/comments/q7mgpa/difference_between_char_signed_char_unsigned_char/)
- [c++ - When is uint8_t ≠ unsigned char? - Stack Overflow](https://stackoverflow.com/questions/16138237/when-is-uint8-t-%E2%89%A0-unsigned-char)
- [8位无符号整数应该使用 unsigned char 还是 uint8_t ？ - 知乎](https://www.zhihu.com/question/27812097)
- [c - uint8_t vs unsigned char - Stack Overflow](https://stackoverflow.com/questions/1725855/uint8-t-vs-unsigned-char)
- [uint8_t uint32_t 类型强制转换出错 以及 unsigned char 类型和 unsigned int 类型相互转化_编码小二的赵小二的博客-CSDN博客](https://blog.csdn.net/fightingboom/article/details/102730040)
