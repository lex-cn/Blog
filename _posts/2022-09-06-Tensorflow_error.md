---
title     :
tags      :
categories:
excerpt   : 此处写摘要
mathjax   : true
published : true
toc       : true
---

## tensorflow.python.framework.errors_impl.ResourceExhaustedError: failed to allocate memory [Op:Mul]

显卡的内存耗尽了，解决途径有以下几种措施:

- 减少Batch 的大小
- 分析错误的位置，在哪一层出现显卡不够，比如在全连接层出现的，则降低全连接层的维度，把2048改成1042啥的
- 增加pool层，降低整个网络的维度。
- 修改输入图片的大小

总结以下：想进一切办法降维，降低网络的维度。

另一种情况是同时运行了多个tensorflow程序。由于tensorflow默认是独占CPU的，因此不能同时跑多个程序，否则会出现显卡内存不够的情况。

因此需要进行设置来限制单个程序对GPU的使用。具体的数值需要尝试。太小会导致程序执行失败，返回Dst错误。