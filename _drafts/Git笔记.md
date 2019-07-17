# git status中文乱码

linux下git默认对于中文的支持不是很好，比较突出的就是git status显示的中文文件名
全是“\344\272\247\345\223\201\351\234\200\346\261\202”之类的代码

解决这个问题方法是：

git config --global core.quotepath false

# warning: LF will be replaced by CRLF in XXXXXXXXXXXXXX.

在repo文件目录下执行

```bash
git config core.autocrlf false
```

# 如何下载Github上某个库的分支

以rtklib为例
```
git clone https://github.com/tomojitakasu/RTKLIB.git --depth=1 -b rtklib_2.4.3
```

# QT_STATIC_CONST does not name a type

改成const 和static const

# error: ‘constexpr’ needed for in-class initialization of static data member ‘
# ***’ of non-integral type [-fpermissive] 

constexpr是C14 标准里面的一个关键词，后来又被废除了，呵呵呵呵


# 删除未跟踪的文件和文件夹 git clean

```bash
git clean -f #删除未跟踪的文件
git clean -d #删除未跟踪的文件夹
git clean -n #在删除前提示删除那些文件
git clean -dnf
```

## git remote

```bash
git remote -v 显示远程仓库地址
```

## git stage 与git add 有什么区别
