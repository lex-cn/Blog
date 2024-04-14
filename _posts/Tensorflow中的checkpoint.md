---
title     : Tensorflow训练过程当中保存模型
tags      :
categories:
excerpt   : 此处写摘要
mathjax   : true
published : true
toc       : true
---


Tensorflow训练过程当中保存模型，通过一个回调函数来完成。

回调函数可以是自定义的，当然也可以使用 Tensorflow 当中自带的函数。


```python
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

# Train the model with the new callback
model.fit(train_images,
          train_labels,
          epochs=10,
          validation_data=(test_images, test_labels),
          callbacks=[cp_callback])  # Pass callback to training
```

但当我们想每隔 N 个 epochs 的时候，保存一个模型，那么可以使用peroid参数。

但是peroid参数即将被废弃，所以他们推荐使用`save_freq`，但这个参数的设置需要计算每个epoch当中的计算步骤数nstep，经过我的测试

$$nstep =int(len(Data)/batchsize)+1 $$

其中Data是训练数据，但注意`model.fit()`中`validation_split`。这个参数说明每次训练都有一部分数据拿出来作为当个历元的验证集，所以每个历元的正常参与训练的数据只有总数据量的(1-validation_split)


- https://tensorflow.google.cn/guide/checkpoint
- https://www.w3cschool.cn/tensorflow_python/tf_keras_callbacks_ModelCheckpoint.html
- https://blog.csdn.net/youzhizhe2014/article/details/103488205
- https://stackoverflow.com/questions/59069058/save-model-every-10-epochs-tensorflow-keras-v2
- https://stackoverflow.com/questions/66355298/keras-modelcheckpoint-can-save-freq-period-change-dynamically
- https://stackoverflow.com/questions/70368770/how-to-create-checkpoint-filenames-with-epoch-or-batch-number-when-using-modelch

