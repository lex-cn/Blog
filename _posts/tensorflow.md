
## tf.pad

https://tensorflow.google.cn/guide/data?hl=zh_cn#batching_tensors_with_padding
[tf.pad 用法说明 - 走看看](http://t.zoukankan.com/happy-sir-p-11637824.html)
[tensorflow学习013——tf.data模块简介及用法 - 白菜茄子 - 博客园](https://www.cnblogs.com/sunjianzhao/p/15581295.html)

[torch.Tensor.expand详解_jeremysun1224的博客-CSDN博客_torch.expand](https://blog.csdn.net/Kobe2113751293/article/details/108188309)
[torch.Tensor.fill_(value)方法_人类高质量算法工程师的博客-CSDN博客](https://blog.csdn.net/qq_35037684/article/details/113769542)
[tf.pad函数_不负韶华ღ的博客-CSDN博客_pad函数](https://blog.csdn.net/weixin_49346755/article/details/124885072)[torch.Tensor.fill_(value)方法_人类高质量算法工程师的博客-CSDN博客](https://blog.csdn.net/qq_35037684/article/details/113769542)
[tf.pad函数功能介绍_无尽的沉默的博客-CSDN博客_pad函数](https://blog.csdn.net/hgnuxc_1993/article/details/117263248)
[tf.pad 用法说明 - 剪掉辫子的人 - 博客园](https://www.cnblogs.com/happy-sir/p/11637824.html)
[神经网络学习-tensorflow2.0-tensor的合并与分割 - ladadee - 博客园](https://www.cnblogs.com/ladade/p/13798924.html)

[多个tensor合并成一个——四个三维tensor合成一个四维tensor——四个[3,512,1024]变成[4,3,512,1024]_captain飞虎大队的博客-CSDN博客_tensor合并](https://blog.csdn.net/weixin_41529093/article/details/120224788)

[TensorFlow 辨异 —— tf.add(a, b) 与 a+b（tf.assign 与 =）、tf.nn.bias_add 与 tf.add - 简书](https://www.jianshu.com/p/a016d3dde1a6)


## TFrecord


[How to train a Keras model on TFRecord files](https://keras.io/examples/keras_recipes/tfrecord/#define-loading-methods)
[TFRecord 简介 | 来呀，快活呀~](https://xmfbit.github.io/2020/04/03/tfrecord-introduction/)
[TensorFlow Data模块](https://www.bbsmax.com/A/q4zVY06GdK/)
[TFRecord的Shuffle、划分和读取 - 多事鬼间人 - 博客园](https://www.cnblogs.com/yc0806/p/16526114.html)
[Tensorflow之tfrecord加载数据与模型训练_bineleanor的博客-CSDN博客_用tfrecord文件训练](https://blog.csdn.net/z2536083458/article/details/96769254)
[TensorFlow2.0 TFrecord数据集的写入、读取和训练示例详解_Monalena的博客-CSDN博客_tensorflow2 读取tfrecord](https://blog.csdn.net/sweetwind1996/article/details/103361915/)
[Tensorflow2.0进阶学习-分布式自定义循环训练 (十)_赫凯的博客-CSDN博客_tensorflow2.0 分布式训练](https://blog.csdn.net/u010095372/article/details/124569877)
[tf.data.TFRecordDataset  |  TensorFlow v2.10.0](https://tensorflow.google.cn/api_docs/python/tf/compat/v1/TFRecordReader)
[Parameter server training with ParameterServerStrategy  |  TensorFlow Core](https://tensorflow.google.cn/tutorials/distribute/parameter_server_training)
[TensorFlow基础（十二）——制作tfrecord训练集-蒲公英云](https://www.dandelioncloud.cn/article/details/1471333779586506753)


## Tensorboard

[详解Tensorboard及使用教程_八岁爱玩耍的博客-CSDN博客_tensorboard](https://blog.csdn.net/weixin_53598445/article/details/121301078)
[Migrate TensorBoard: TensorFlow's visualization toolkit  |  TensorFlow Core](https://tensorflow.google.cn/guide/migrate/tensorboard)
[Get started with TensorBoard  |  TensorFlow](https://tensorflow.google.cn/tensorboard/get_started)



## LearningRateScheduler

经验表明，刚开始训练的时候，学习率可以大一点；随着训练的进行，学习率可以逐步降低。这样做主要是为了防止出现局部伪最优。

在训练中后期，过大的LR可能导致模型在最优解附近震荡，无法快速收敛。

因此，可以根据学习的历元数量来逐步降低学习率。

keras.callbacks提供了LearningRateScheduler函数。使用方式如下：

- class CosineDecay: A LearningRateSchedule that uses a cosine decay schedule.
- class CosineDecayRestarts: A LearningRateSchedule that uses a cosine decay schedule with restarts.
- class ExponentialDecay: A LearningRateSchedule that uses an exponential decay schedule.
- class InverseTimeDecay: A LearningRateSchedule that uses an inverse time decay schedule.
- class LearningRateSchedule: The learning rate schedule base class.
- class PiecewiseConstantDecay: A LearningRateSchedule that uses a piecewise constant decay schedule.
- class PolynomialDecay: A LearningRateSchedule that uses a polynomial decay schedule.

- [TensorFlow.Keras Learning rate schedule - 知乎](https://zhuanlan.zhihu.com/p/416446400)
- [Learning Rate Schedule：CNN学习率调整策略 - 知乎](https://zhuanlan.zhihu.com/p/410971793)

## has no attribute

这个问题，一般是版本号问题导致的。

tensorflow, Keras, 和Cudnn的版本号一定要对应。

keras和tensorflow内置的keras混用导致冲突。

[cuda和tensorflow的版本对应关系\_捌椒的博客-CSDN博客](https://blog.csdn.net/qq_40926887/article/details/123900382)


