# warning C4706: assignment within conditional expression

这是一个L4级别的警告。有些时候在if语句的判断表达式中，“=”和“==”d都是有意义的，程序员又容易将二者弄错，因此编译器就用警告信息提醒程序员是否弄错。

```
warning C4706: assignment within conditional expression
```

比如说下列代码中

```c
    extern int satid2no(const char *id); // satid2no的原型


    int sat;
    ...// balabala
    if (!(sat=satid2no(exsatid))) continue;
    ...// balabala
```
这里的意思是获取sat的值，如果sat不为0，那么程序继续下一步。此处就会产生一个警告。这样写也不算不对，但是如果写成下面这种形式

```c
    if (!(sat==satid2no(exsatid))) continue;
```

这个错误将会不容易识别出来。编译肯定会通过，但是程序的意义就变了。
