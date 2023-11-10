
## Tensorflow的内存问题

## 对象转换



## Tensorflow的版本匹配问题

Tensorflow的开发速度较快，不同版本的Tensorflow在保存和加载模型的过程中可能产生多种错误，例如

```
ValueError: Layer 'conv2d_1' expected 2 variables, but received 0 variables during loading

ValueError: Layer 'conv1_conv' expected 1 variables, but received 0 variables during loading. Expected: ['kernel']
```

在github issue上已经有人对此事进行了反馈

```
This is now fixed at HEAD but the issue will persist in TF 2.13 and TF 2.14. Use get_weights()/set_weights() as a workaround.
```

[python 3.x - ValueError: Layer 'lstm\_cell\_2' expected 3 variables, but received 0 variables during loading - Stack Overflow](https://stackoverflow.com/questions/76266596/valueerror-layer-lstm-cell-2-expected-3-variables-but-received-0-variables-d)

[Saving broken between tf.keras and Keras Core · Issue #855 · keras-team/keras-core](https://github.com/keras-team/keras-core/issues/855)

最简单的办法是将使用模型训练时的tensroflow版本。**如果不知道keras/h5文件的具体版本，可以将文件以文本模式直接打开，可以看到具体的模型版本**