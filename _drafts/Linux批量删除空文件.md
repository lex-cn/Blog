

Linux中find批量删除空文件及空文件夹脚本_lppl010_的专栏-CSDN博客_linux删除所有空目录

### Linux种批量删除空文件

Linux下批量删除空文件（大小等于0的文件）的方法


```bash
find . -name "*" -type f -size 0c | xargs -n 1 rm -f
```

用这个还可以删除指定大小的文件，只要修改对应的 -size 参数就行，例如：

```bash
find . -name "shuaige.txt" -exec rm -f {}
```

删除前有提示 

```bash
find . -name "shuaige.txt" -ok rm -rf {} ;
```
   
删除当前目录下面所有 test 文件夹下面的文件 

```bash
find . -name "test" -type d -exec rm -rf {} ;
```

删除文件夹下面的所有的.svn文件

```bash
find . -name '.svn' -exec rm -rf {} ;
```

注:

1. `{}`和之间有一个空格 
2. find . -name 之间也有空格 
3. exec 是一个后续的命令,{}内的内容代表前面查找出来的文件

- [Linux中find批量删除空文件及空文件夹脚本_lppl010_的专栏-CSDN博客_linux删除所有空目录](https://blog.csdn.net/lppl010_/article/details/80733651)


### Linux统计程序运行时间


```bash
time sh xxx.sh
```


[Linux 使用 time sh 统计程序运行时间_Robin_Pi的博客-CSDN博客](https://blog.csdn.net/Robin_Pi/article/details/108772239)
