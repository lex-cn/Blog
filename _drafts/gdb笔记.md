

# gdb命令行选项

```bash
gdb -x filename  # 从脚本启动
```

# gdb内的操作

```gdb
show args  #显示输入的变量
until      #跳出循环
list       #显示10行代码
list n     #显示第n行前后10行的代码
```

# optimized out

gdb调试查看变量的值的时候,出现<optimized out>

解决方法是将:

    -O3或者其他的数字
    //修改为0
    -O0//意思是不进行优化

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

