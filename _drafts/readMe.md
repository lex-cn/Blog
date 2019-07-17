# Linux操作及问题笔记

linux下查看进程运行的时间
```bash
ps -eo pid,tty,user,comm,lstart,etime | grep init
```

linux 下取进程占用内存(MEM)最高的前10个进程

# linux 下取进程占用 cpu 最高的前10个进程

```bash
ps aux|head -1;ps aux|grep -v PID|sort -rn -k +3|head
```

# linux 下取进程占用内存(MEM)最高的前10个进程

```bash
ps aux|head -1;ps aux|grep -v PID|sort -rn -k +4|head
```

# Transport endpoint is not connected 的解决办法

在使用sshfs挂载一个远程目录时，

```bash
ls: cannot access 'shfs': Transport endpoint is not connected
total 135M
-rw-r--r--  1 lex lex    0 Mar  8 10:35 atex
drwxr-xr-x 15 lex lex 4.0K May 15 20:44 Documents
d?????????  ? ?   ?      ?            ? shfs
-rw-------  1 lex lex  13M May  9 22:58 nohup.out
drwxr-xr-x  3 lex lex 4.0K Mar  6  2017 R
drwxr-xr-x  3 lex lex 4.0K Feb 27 19:40 Software
drwxr-xr-x  5 lex lex 4.0K Apr 10 20:46 Temp
drwxr-xr-x  3 lex lex 4.0K Apr 30 16:56 tmp
drwxr-xr-x  6 lex lex 4.0K Mar  6 22:13 toDelete
```

I get this message when there's been a bad *disconnect* from a fuse fs.

Unmounting and remounting the fs solves it

Code:

```bash
$ fusermount -u <mountpoint>
$ sshfs <mountpoint>
```


https://www.linuxquestions.org/questions/slackware-14/transport-endpoint-is-not-connected-filesystem-error-817146/

# VLC is unable to open the MRL

samba 

如果是打开samba共享文件时出现的，主要的解决办法如下

[参考链接1](https://askubuntu.com/questions/618204/cannot-play-files-over-samba-share-on-mate-15-04)

[参考链接2](https://ubuntu-mate.community/t/solved-question-on-network-drives/1210/6)
