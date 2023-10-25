---
created: 2023-08-24T16:33:41 (UTC +08:00)
tags: [tensorflow2.0能自动调动gpu吗]
source: https://blog.csdn.net/qq_36758914/article/details/107152997
author: 成就一亿技术人!
---

# Tensorflow2.0 之开启 GPU 模式_tensorflow2.0能自动调动gpu吗_cofisher的博客-CSDN博客

> ## Excerpt
> GPU 的使用以及与 CPU 的对比_tensorflow2.0能自动调动gpu吗

---
### 文章目录

-   [一、查看设备是否有合适的 GPU](https://blog.csdn.net/qq_36758914/article/details/107152997#_GPU_1)
-   [二、日志设备放置](https://blog.csdn.net/qq_36758914/article/details/107152997#_12)
-   [三、为程序指定特定的 GPU](https://blog.csdn.net/qq_36758914/article/details/107152997#_GPU_18)
-   [四、内存分配](https://blog.csdn.net/qq_36758914/article/details/107152997#_24)
-   -   [1、按需分配](https://blog.csdn.net/qq_36758914/article/details/107152997#1_25)
    -   [2、设置 GPU 显存为固定使用量](https://blog.csdn.net/qq_36758914/article/details/107152997#2_GPU__32)
-   [五、显式指定 GPU](https://blog.csdn.net/qq_36758914/article/details/107152997#_GPU_39)
-   [六、多 GPU 的使用](https://blog.csdn.net/qq_36758914/article/details/107152997#_GPU__57)
-   [七、GPU vs CPU](https://blog.csdn.net/qq_36758914/article/details/107152997#GPU_vs_CPU_70)

## 一、查看设备是否有合适的 GPU

首先，我们需要先确认所用设备是否支持 Tensorflow-gpu 的使用：

```
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
```

```
Num GPUs Available:  1
```

这说明当前设备中有一个 GPU 可供 Tensorflow 使用。

## 二、日志设备放置

为了查出我们的操作和张量被配置到哪个 GPU 或 CPU 上，我们可以在程序起始位置加上：

```
tf.debugging.set_log_device_placement(True)
```

## 三、为程序指定特定的 GPU

如果想要在所有 GPU 中指定只使用第一个 GPU，那么需要添加以下语句。

```
tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
```

## 四、内存分配

## 1、按需分配

第一个选项是通过调用 tf.config.experimental.set\_memory\_growth 来打开内存增长，它试图只分配运行时所需的 GPU 内存：它开始分配非常少的内存，随着程序运行和更多的 GPU 内存需要，我们扩展分配给 Tensorflow 进程的 GPU 内存区域。

```
tf.config.experimental.set_memory_growth(gpu[0], True)
```

## 2、设置 GPU 显存为固定使用量

设置使用第一个 GPU 的显存为 1G。

```
tf.config.experimental.set_virtual_device_configuration(
    gpus[0],
    [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])
```

## 五、显式指定 GPU

如果我们的系统里有不止一个 GPU，则默认情况下，ID 最小的 GPU 将被选用。如果想在不同的 GPU 上运行，我们需要显式地指定优先项。

```
with tf.device("/gpu:0"):
    tf.random.set_seed(0)
    a = tf.random.uniform((10000,10000),minval = 0,maxval = 3.0)
    c = tf.matmul(a, tf.transpose(a))
    d = tf.reduce_sum(c)
```

此处显式指定了使用 GPU 0，如果指定的 GPU 不存在，则程序会报错。

如果希望 TensorFlow 自动选择一个现有且受支持的设备来运行操作，以避免指定的设备不存在，那么可以在程序起始位置加上：

```
tf.config.set_soft_device_placement(True)
```

当然，显式指定使用 CPU 也是可以的，只需要把 tf.device("/gpu:0") 改成 tf.device("/cpu:0") 即可。并且，如果一个 TensorFlow 操作同时具有 CPU 和 GPU 两种实现，在默认情况下，当操作被分配给一个设备时，GPU 设备将被给予优先级。

## 六、多 GPU 的使用

下面是一个简单的例子说明多 GPU 的同时使用：

```
tf.debugging.set_log_device_placement(True)

strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
  inputs = tf.keras.layers.Input(shape=(1,))
  predictions = tf.keras.layers.Dense(1)(inputs)
  model = tf.keras.models.Model(inputs=inputs, outputs=predictions)
  model.compile(loss='mse',
                optimizer=tf.keras.optimizers.SGD(learning_rate=0.2))
```

## 七、GPU vs CPU

```
import tensorflow as tf
from tensorflow.keras import *
import time

tf.config.set_soft_device_placement(True)
tf.debugging.set_log_device_placement(True)

gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)

t=time.time()
with tf.device("/gpu:0"):
    tf.random.set_seed(0)
    a = tf.random.uniform((10000,10000),minval = 0,maxval = 3.0)
    c = tf.matmul(a, tf.transpose(a))
    d = tf.reduce_sum(c)
print('gpu: ', time.time()-t)

t=time.time()
with tf.device("/cpu:0"):
    tf.random.set_seed(0)
    a = tf.random.uniform((10000,10000),minval = 0,maxval = 3.0)
    c = tf.matmul(a, tf.transpose(a))
    d = tf.reduce_sum(c)
print('cpu: ', time.time()-t)
```

```
Executing op RandomUniform in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Sub in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Mul in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Add in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Transpose in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Sum in device /job:localhost/replica:0/task:0/device:GPU:0
gpu:  0.9708232879638672
Executing op RandomUniform in device /job:localhost/replica:0/task:0/device:CPU:0
Executing op Sub in device /job:localhost/replica:0/task:0/device:CPU:0
Executing op Mul in device /job:localhost/replica:0/task:0/device:CPU:0
Executing op Add in device /job:localhost/replica:0/task:0/device:CPU:0
Executing op Transpose in device /job:localhost/replica:0/task:0/device:CPU:0
Executing op MatMul in device /job:localhost/replica:0/task:0/device:CPU:0
Executing op Sum in device /job:localhost/replica:0/task:0/device:CPU:0
cpu:  4.51805853843689
```

可见使用 GPU 进行以上运算会比 CPU 快将近 5 倍。


---
created: 2023-09-12T17:53:06 (UTC +08:00)
tags: []
source: https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration
author:
---

# tf.config.set_logical_device_configuration  |  TensorFlow v2.13.0

> ## Excerpt
> Set the logical device configuration for a tf.config.PhysicalDevice.

---
Set the logical device configuration for a [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice).

#### View aliases

**Main aliases**

[`tf.config.experimental.set_virtual_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate) for more details.

[`tf.compat.v1.config.experimental.set_virtual_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration), [`tf.compat.v1.config.set_logical_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration)

```
tf.config.set_logical_device_configuration(    device, logical_devices)
```

### Used in the notebooks

A visible [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice) will by default have a single [`tf.config.LogicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDevice) associated with it once the runtime is initialized. Specifying a list of [`tf.config.LogicalDeviceConfiguration`](https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration) objects allows multiple devices to be created on the same [`tf.config.PhysicalDevice`](https://www.tensorflow.org/api_docs/python/tf/config/PhysicalDevice).

Logical device configurations can be modified by calling this function as long as the runtime is uninitialized. After the runtime is initialized calling this function raises a RuntimeError.

The following example splits the CPU into 2 logical devices:

```
physical_devices = tf.config.list_physical_devices('CPU')
```

The following example splits the GPU into 2 logical devices with 100 MB each:

```
physical_devices = tf.config.list_physical_devices('GPU')
```

<table><colgroup><col width="214px"><col></colgroup><tbody><tr><th colspan="2"><h2 id="args" data-text="Args" role="presentation"><span role="heading" aria-level="2">Args</span></h2></th></tr><tr><td><code translate="no" dir="ltr">device</code><a id="device"></a></td><td>The <code translate="no" dir="ltr">PhysicalDevice</code> to configure.</td></tr><tr><td><code translate="no" dir="ltr">logical_<wbr>devices</code><a id="logical_devices"></a></td><td>(optional) List of <a href="https://www.tensorflow.org/api_docs/python/tf/config/LogicalDeviceConfiguration"><code translate="no" dir="ltr">tf.config.LogicalDeviceConfiguration</code></a> objects to allocate for the specified <code translate="no" dir="ltr">PhysicalDevice</code>. If None, the default configuration will be used.</td></tr></tbody></table>

<table><colgroup><col width="214px"><col></colgroup><tbody><tr><th colspan="2"><h2 id="raises" data-text="Raises">Raises</h2></th></tr><tr><td><code translate="no" dir="ltr">ValueError</code><a id="ValueError"></a></td><td>If argument validation fails.</td></tr><tr><td><code translate="no" dir="ltr">RuntimeError</code><a id="RuntimeError"></a></td><td>Runtime is already initialized.</td></tr></tbody></table>


---
created: 2023-09-12T17:53:00 (UTC +08:00)
tags: []
source: https://www.tensorflow.org/guide/gpu?hl=zh-cn
author:
---

# 使用 GPU  |  TensorFlow Core

> ## Excerpt
> 无需更改任何代码，TensorFlow 代码以及 tf.keras 模型就可以在单个 GPU 上透明运行。

---
无需更改任何代码，TensorFlow 代码以及 [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras?hl=zh-cn) 模型就可以在单个 GPU 上透明运行。

注：使用 `tf.config.list_physical_devices('GPU')` 可以确认 TensorFlow 使用的是 GPU。

在一台或多台机器上，要顺利地在多个 GPU 上运行，最简单的方法是使用[分布策略](https://render.githubusercontent.com/view/distributed_training.ipynb)。

本指南适用于已尝试这些方法，但发现需要对 TensorFlow 使用 GPU 的方式进行精细控制的用户。要了解如何为单 GPU 和多 GPU 情景调试性能问题，请参阅[优化 TensorFlow GPU 性能](https://www.tensorflow.org/guide/gpu_performance_analysis?hl=zh-cn)指南。

## 设置

确保已安装最新的 TensorFlow GPU 版本。

```
import tensorflow as tfprint("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
```

```
2022-12-14 22:45:50.077454: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2022-12-14 22:45:50.077552: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2022-12-14 22:45:50.077562: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
Num GPUs Available:  4

```

## 概述

TensorFlow 支持在各种类型的设备上执行计算，包括 CPU 和 GPU。我们使用字符串标识符来表示这些设备，例如：

-   `"/device:CPU:0"`：机器的 CPU。
-   `"/GPU:0"`：TensorFlow 可见的机器上第一个 GPU 的速记表示法。
-   `"/job:localhost/replica:0/task:0/device:GPU:1"`：TensorFlow 可见的机器上第二个 GPU 的完全限定名称。

如果一个 TensorFlow 运算同时有 CPU 和 GPU 实现，则在默认情况下，分配运算时会优先使用 GPU 设备。例如，[`tf.matmul`](https://www.tensorflow.org/api_docs/python/tf/linalg/matmul?hl=zh-cn) 同时有 CPU 和 GPU 内核，在具有 `CPU:0` 和 `GPU:0` 设备的系统上，将选择 `GPU:0` 设备来运行 `tf.matmul`，除非明确要求在另一个设备上运行。

如果一个 TensorFlow 运算没有相应的 GPU 实现，则该运算将回退到 CPU 设备。例如，由于 [`tf.cast`](https://www.tensorflow.org/api_docs/python/tf/cast?hl=zh-cn) 只有一个 CPU 内核，在具有 `CPU:0` 和 `GPU:0` 设备的系统上，即使请求在 `GPU:0` 设备上运行 `tf.cast`，也会选择 `CPU:0` 设备来运行该运算。

## 记录设备放置

为了找出将运算和张量分配到的目标设备，请将 [`tf.debugging.set_log_device_placement(True)`](https://www.tensorflow.org/api_docs/python/tf/debugging/set_log_device_placement?hl=zh-cn) 放在程序的第一行。启用设备放置记录将导致任何张量分配或运算被打印。

```
tf.debugging.set_log_device_placement(True)# Create some tensorsa = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])c = tf.matmul(a, b)print(c)
```

```
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0
tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)

```

以上代码将打印 `MatMul` 运算在 `GPU:0` 上执行的指示。

## 手动设备放置

如果您希望在自己选择的设备上执行特定运算，而不是在自动选择的设备上执行，则可以使用 `with tf.device` 创建设备上下文。创建完成后，该上下文中的所有运算都会在同一指定设备上运行。

```
tf.debugging.set_log_device_placement(True)# Place tensors on the CPUwith tf.device('/CPU:0'):  a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])  b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])c = tf.matmul(a, b)print(c)
```

```
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0
tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)

```

现在，您会看到已将 `a` 和 `b` 分配给 `CPU:0`。由于没有为 `MatMul` 运算明确指定设备，TensorFlow 运行时将根据运算和可用的设备选择一个设备（本例中为 `GPU:0`），并且在需要时会自动在设备之间复制张量。

## 限制 GPU 内存增长

默认情况下，TensorFlow 会映射进程可见的所有 GPU（取决于 [`CUDA_VISIBLE_DEVICES`](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#env-vars)）的几乎全部内存。这是为了减少内存碎片，更有效地利用设备上相对宝贵的 GPU 内存资源。为了将 TensorFlow 限制为使用一组特定的 GPU，我们使用 [`tf.config.set_visible_devices`](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices?hl=zh-cn) 方法。

```
gpus = tf.config.list_physical_devices('GPU')if gpus:  # Restrict TensorFlow to only use the first GPU  try:    tf.config.set_visible_devices(gpus[0], 'GPU')    logical_gpus = tf.config.list_logical_devices('GPU')    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPU")  except RuntimeError as e:    # Visible devices must be set before GPUs have been initialized    print(e)
```

```
Visible devices cannot be modified after being initialized

```

在某些情况下，我们希望进程最好只分配可用内存的一个子集，或者仅在进程需要时才增加内存使用量。TensorFlow 为此提供了两种控制方法。

第一个选项是通过调用 [`tf.config.experimental.set_memory_growth`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth?hl=zh-cn) 来开启内存增长。此选项会尝试根据运行时分配的需求分配尽可能充足的 GPU 内存：首先分配非常少的内存，随着程序的运行，需要的 GPU 内存逐渐增多，于是扩展 TensorFlow 进程的 GPU 内存区域。内存不会被释放，因为这样会产生内存碎片。要关闭特定 GPU 的内存增长，请在分配任何张量或执行任何运算之前使用以下代码。

```
gpus = tf.config.list_physical_devices('GPU')if gpus:  try:    # Currently, memory growth needs to be the same across GPUs    for gpu in gpus:      tf.config.experimental.set_memory_growth(gpu, True)    logical_gpus = tf.config.list_logical_devices('GPU')    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")  except RuntimeError as e:    # Memory growth must be set before GPUs have been initialized    print(e)
```

```
Physical devices cannot be modified after being initialized

```

第二个启用此选项的方式是将环境变量 `TF_FORCE_GPU_ALLOW_GROWTH` 设置为 `true`。这是一个特定于平台的配置。

第二种方法是使用 [`tf.config.set_logical_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration?hl=zh-cn) 配置虚拟 GPU 设备，并且设置可在 GPU 上分配多少总内存的硬性限制。

```
gpus = tf.config.list_physical_devices('GPU')if gpus:  # Restrict TensorFlow to only allocate 1GB of memory on the first GPU  try:    tf.config.set_logical_device_configuration(        gpus[0],        [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])    logical_gpus = tf.config.list_logical_devices('GPU')    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")  except RuntimeError as e:    # Virtual devices must be set before GPUs have been initialized    print(e)
```

```
Virtual devices cannot be modified after being initialized

```

这在要真正限制可供 TensorFlow 进程使用的 GPU 内存量时非常有用。在本地开发中，与其他应用（如工作站 GUI）共享 GPU 时，这是常见做法。

## 使用多 GPU 系统上的单个 GPU

如果系统上有多个 GPU，则默认情况下会选择具有最小 ID 的 GPU。如果希望在不同的 GPU 上运行，则需要明确指定需要的 GPU：

```
tf.debugging.set_log_device_placement(True)try:  # Specify an invalid GPU device  with tf.device('/device:GPU:2'):    a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])    b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])    c = tf.matmul(a, b)except RuntimeError as e:  print(e)
```

```
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:2

```

如果指定的设备不存在，则会引发 `RuntimeError` 错误：`.../device:GPU:2 unknown device`。

当指定的设备不存在时，如果希望 TensorFlow 自动选择存在且支持的设备来执行运算，可以调用 [`tf.config.set_soft_device_placement(True)`](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement?hl=zh-cn)。

```
tf.config.set_soft_device_placement(True)tf.debugging.set_log_device_placement(True)# Creates some tensorsa = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])c = tf.matmul(a, b)print(c)
```

```
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0
tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)

```

## 使用多个 GPU

为多个 GPU 开发的模型可使用额外的资源进行扩展。如果在具有单个 GPU 的系统上进行开发，可以使用虚拟设备模拟多个 GPU。这样，无需额外的资源，您就可以轻松对多 GPU 设置进行测试。

```
gpus = tf.config.list_physical_devices('GPU')if gpus:  # Create 2 virtual GPUs with 1GB memory each  try:    tf.config.set_logical_device_configuration(        gpus[0],        [tf.config.LogicalDeviceConfiguration(memory_limit=1024),         tf.config.LogicalDeviceConfiguration(memory_limit=1024)])    logical_gpus = tf.config.list_logical_devices('GPU')    print(len(gpus), "Physical GPU,", len(logical_gpus), "Logical GPUs")  except RuntimeError as e:    # Virtual devices must be set before GPUs have been initialized    print(e)
```

```
Virtual devices cannot be modified after being initialized

```

建立可供运行时使用的多个逻辑 GPU 后，可以通过 [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy?hl=zh-cn) 或手动放置来利用多个 GPU。

#### 使用 [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy?hl=zh-cn)

使用多个 GPU 的最佳做法是使用 [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy?hl=zh-cn)。下面是一个简单示例：

```
tf.debugging.set_log_device_placement(True)gpus = tf.config.list_logical_devices('GPU')strategy = tf.distribute.MirroredStrategy(gpus)with strategy.scope():  inputs = tf.keras.layers.Input(shape=(1,))  predictions = tf.keras.layers.Dense(1)(inputs)  model = tf.keras.models.Model(inputs=inputs, outputs=predictions)  model.compile(loss='mse',                optimizer=tf.keras.optimizers.SGD(learning_rate=0.2))
```

```
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:GPU:0', '/job:localhost/replica:0/task:0/device:GPU:1', '/job:localhost/replica:0/task:0/device:GPU:2', '/job:localhost/replica:0/task:0/device:GPU:3')
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op StatelessRandomGetKeyCounter in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op StatelessRandomUniformV2 in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Sub in device /job:localhost/replica:0/task:0/device:GPU:0
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
_EagerConst: (_EagerConst): /job:localhost/replica:0/task:0/device:GPU:0
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
a: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
b: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
MatMul: (MatMul): /job:localhost/replica:0/task:0/device:GPU:0
product_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
_EagerConst: (_EagerConst): /job:localhost/replica:0/task:0/device:GPU:2
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
a: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
b: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
MatMul: (MatMul): /job:localhost/replica:0/task:0/device:GPU:2
product_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
_EagerConst: (_EagerConst): /job:localhost/replica:0/task:0/device:GPU:1
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:1
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:1
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:2
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:2
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
_EagerConst: (_EagerConst): /job:localhost/replica:0/task:0/device:GPU:3
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:3
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:3
input: (_Arg): /job:localhost/replica:0/task:0/device:CPU:0
_EagerConst: (_EagerConst): /job:localhost/replica:0/task:0/device:GPU:0
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
seed: (_Arg): /job:localhost/replica:0/task:0/device:CPU:0
StatelessRandomGetKeyCounter: (StatelessRandomGetKeyCounter): /job:localhost/replica:0/task:0/device:GPU:0
key_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
counter_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
shape: (_DeviceArg): /job:localhost/replica:0/task:0/device:CPU:0
key: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
counter: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
alg: (_DeviceArg): /job:localhost/replica:0/task:0/device:CPU:0
StatelessRandomUniformV2: (StatelessRandomUniformV2): /job:localhost/replica:0/task:0/device:GPU:0
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
x: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
y: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
Sub: (Sub): /job:localhost/replica:0/task:0/device:GPU:0
z_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
x: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
y: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
Mul: Executing op Mul in device /job:localhost/replica:0/task:0/device:GPU:0
(Mul): /job:localhost/replica:0/task:0/device:GPU:0
z_RetVal: (_Retval): /job:localhost/replica:Executing op AddV2 in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Fill in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
0/task:0/device:GPU:0
x: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
y: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
AddV2: (AddV2): /job:localhost/replica:0/task:0/device:GPU:0
z_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
ReadVariableOp: (ReadVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
value_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
Identity: (Identity): /job:localhost/replica:0/task:0/device:GPU:1
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:1
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:1
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
Identity: (Identity): /job:localhost/replica:0/task:0/device:GPU:2
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:2
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:2
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
Identity: (Identity): /job:localhost/replica:0/task:0/device:GPU:3
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:3
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:3
NoOp: (NoOp): /job:localhost/replica:0/task:0/device:GPU:0
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
Identity: (Identity): /job:localhost/replica:0/task:0/device:GPU:0
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
dims: (_DeviceArg): /job:localhost/replica:0/task:0/device:CPU:0
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
Fill: (Fill): /job:localhost/replica:0/task:0/device:GPU:0
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
ReadVariableOp: (ReadVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
value_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:1
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:1
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:2
resource: (_Arg): /job:localhost/replica:0/taskExecuting op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Fill in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
INFO:tensorflow:Reduce to /job:localhost/replica:0/task:0/device:CPU:0 then broadcast to ('/job:localhost/replica:0/task:0/device:CPU:0',).
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
:0/device:GPU:2
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:2
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:3
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:3
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
_EagerConst: (_EagerConst): /job:localhost/replica:0/task:0/device:GPU:0
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
ReadVariableOp: (ReadVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
value_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
Identity: (Identity): /job:localhost/replica:0/task:0/device:GPU:1
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:1
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:1
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
Identity: (Identity): /job:localhost/replica:0/task:0/device:GPU:2
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:2
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:2
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
Identity: (Identity): /job:localhost/replica:0/task:0/device:GPU:3
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:3
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:3
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
ReadVariableOp: (ReadVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
value_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
ReadVariableOp: (ReadVariableOp): /job:localhost/replica:0/task:0/device:GPU:1
value_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
ReadVariableOp: (ReadVariableOp): /job:localhost/replica:0/task:0/device:GPU:2
value_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
ReadVariableOp: (ReadVariableOp): /job:localhost/replica:0/task:0/device:GPU:3
value_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
inputs_0: (_Arg): /job:localhost/replica:0/task:0/device:CPU:0
inputs_1: (_Arg): /job:localhost/replica:0/task:0/device:CPU:0
inputs_2: (_Arg): /job:localhost/replica:0/task:0/device:CPU:0
inputs_3: (_Arg): /job:localhost/replica:0/task:0/device:CPU:0
AddN: (AddN): /job:localhost/replica:0/task:0/device:CPU:0
sum_RetVExecuting op AddN in device /job:localhost/replica:0/task:0/device:CPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:CPU:0
INFO:tensorflow:Reduce to /job:localhost/replica:0/task:0/device:CPU:0 then broadcast to ('/job:localhost/replica:0/task:0/device:CPU:0',).
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AddN in device /job:localhost/replica:0/task:0/device:CPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:CPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Fill in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
INFO:tensorflow:Reduce to /job:localhost/replica:0/task:0/device:CPU:0 then broadcast to ('/job:localhost/replica:0/task:0/device:CPU:0',).
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AddN in device /job:localhost/replica:0/task:0/device:CPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:CPU:0
INFO:tensorflow:Reduce to /job:localhost/replica:0/task:0/device:CPU:0 then broadcast to ('/job:localhost/replica:0/task:0/device:CPU:0',).
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AddN in device /job:localhost/replica:0/task:0/device:CPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:CPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0

```

此程序会在每个 GPU 上运行模型的一个副本，并将输入数据拆分到每个 GPU 上，也就是所谓的“[数据并行](https://en.wikipedia.org/wiki/Data_parallelism)”。

有关分布策略的详细信息，请查阅[此处](https://render.githubusercontent.com/view/distributed_training.ipynb)的指南。

#### 手动放置

[`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy?hl=zh-cn) 通过跨设备复制计算在后台运行。您可以通过在每个 GPU 上构建模型来手动实现复制。例如：

```
tf.debugging.set_log_device_placement(True)gpus = tf.config.list_logical_devices('GPU')if gpus:  # Replicate your computation on multiple GPUs  c = []  for gpu in gpus:    with tf.device(gpu.name):      a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])      b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])      c.append(tf.matmul(a, b))with tf.device('/CPU:0'):    matmul_sum = tf.add_n(c)print(matmul_sum)
```

```
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AddN in device /job:localhost/replica:0/task:0/device:CPU:0
tf.Tensor(
[[ 88. 112.]
 [196. 256.]], shape=(2, 2), dtype=float32)

```

---
created: 2023-08-24T16:33:32 (UTC +08:00)
tags: [跑Tensorflow模型设置用GPU的一些总结]
source: https://blog.csdn.net/qq_42250789/article/details/107070520
author: 成就一亿技术人!
---

# 跑Tensorflow模型设置用GPU的一些总结_cv_lz的博客-CSDN博客

> ## Excerpt
> 一、用如下代码可以看用tensorflow框架跑深度学习模型时用CPU还是GPU:from tensorflow.python.client import device_lib print(device_lib.list_local_devices())结果显示情况:可以看出在用一个CPU设备跑代码，接下来查看tensorflow版本conda list如果tensorflow版本高于tensorflow-gpu版本，则需要更新tensorflow-gpu版本，说明默认选

---
**目录**

[一、查看是否用了GPU跑代码](https://blog.csdn.net/qq_42250789/article/details/107070520#%E4%B8%80%E3%80%81%E6%9F%A5%E7%9C%8B%E6%98%AF%E5%90%A6%E7%94%A8%E4%BA%86GPU%E8%B7%91%E4%BB%A3%E7%A0%81)

[二、用GPU跑代码，观察GPU情况](https://blog.csdn.net/qq_42250789/article/details/107070520#%E4%BA%8C%E3%80%81%E7%94%A8GPU%E8%B7%91%E4%BB%A3%E7%A0%81%EF%BC%8C%E8%A7%82%E5%AF%9FGPU%E6%83%85%E5%86%B5)

[三、设置用GPU跑代码的方法](https://blog.csdn.net/qq_42250789/article/details/107070520#%E4%B8%89%E3%80%81%E8%AE%BE%E7%BD%AE%E7%94%A8GPU%E8%B7%91%E4%BB%A3%E7%A0%81%E7%9A%84%E6%96%B9%E6%B3%95)

[四、查看/安装cuda、cudnn版本](https://blog.csdn.net/qq_42250789/article/details/107070520#%E5%9B%9B%E3%80%81%E6%9F%A5%E7%9C%8B%2F%E5%AE%89%E8%A3%85cuda%E3%80%81cudnn%E7%89%88%E6%9C%AC)

[五、代码一些问题](https://blog.csdn.net/qq_42250789/article/details/107070520#%E4%BA%94%E3%80%81%E4%BB%A3%E7%A0%81%E4%B8%80%E4%BA%9B%E9%97%AE%E9%A2%98)

[错误1：No module named 'tensorflow.contrib'](https://blog.csdn.net/qq_42250789/article/details/107070520#%E9%94%99%E8%AF%AF1%EF%BC%9ANo%20module%20named%20'%20rel=)

[错误2：AttributeError: module 'scipy.misc' has no attribute 'imresize'](https://blog.csdn.net/qq_42250789/article/details/107070520#%E9%94%99%E8%AF%AF2%EF%BC%9AAttributeError%3A%20module%20'%20rel=)

[错误3：](https://blog.csdn.net/qq_42250789/article/details/107070520#%E9%94%99%E8%AF%AF3%EF%BC%9A)

___

## 一、查看是否用了GPU跑代码

用如下代码可以看用tensorflow框架跑深度学习模型时用CPU还是GPU:

```
from tensorflow.python.client import device_libprint(device_lib.list_local_devices())
```

结果显示情况:

![](%E8%B7%91Tensorflow%E6%A8%A1%E5%9E%8B%E8%AE%BE%E7%BD%AE%E7%94%A8GPU%E7%9A%84%E4%B8%80%E4%BA%9B%E6%80%BB%E7%BB%93_cv_lz%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2/x-oss-process=image.png)

可以看出在用一个CPU设备跑代码，接下来查看tensorflow版本

```
conda list
```

如果tensorflow版本高于tensorflow-gpu版本，则需要更新tensorflow-gpu版本，说明默认选择版本高的CPU版本来计算了，升级tensorflow-gpu版本命令为：

```
pip install --index-url http://pypi.douban.com/simple --trusted-host pypi.douban.com --upgrade tensorflow-gpu
```

## 二、用GPU跑代码，观察GPU情况

查看机器上GPU情况 

```
nvidia-smi
```

定时更新显示机器上gpu的情况 

```
nvidia-smi -l
```

设定刷新时间（秒）显示GPU使用情况

```
watch -n 3 nvidia-sm
```

其中左上侧有0、1、2、3的编号，表示GPU的编号，在后面指定GPU时需要使用这个编号。

在终端执行程序时指定GPU    CUDA\_VISIBLE\_DEVICES=0 python main.py

```
 #CUDA_VISIBLE_DEVICES=0,1，2，3  （任意几块）  python  your_file.py  CUDA_VISIBLE_DEVICES=0  python main.py
```

在Python代码中指定GPU  

```
import osos.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"os.environ["CUDA_VISIBLE_DEVICES"] = "0"
```

设置定量的GPU使用量

```
config = tf.ConfigProto() config.gpu_options.per_process_gpu_memory_fraction = 0.9 # 占用GPU90%的显存 session = tf.Session(config=config)
```

设置最小的GPU使用量

```
 config = tf.ConfigProto()  config.gpu_options.allow_growth = True  session = tf.Session(config=config)
```

## 三、设置用GPU跑代码的方法

pycharm运行代码指定GPU的方式大概有两种：

1.在源代码中添加（我没有成功）

```
import os# 指定使用0,1,2三块卡os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2" 
```

2.使用命令行启动程序时加上CUDA\_VISIBLE\_DEVICES=0,1,2
比如, CUDA\_VISIBLE\_DEVICES=0,1,2 python FasterRCNN.py

```
CUDA_VISIBLE_DEVICES=0 python main.py
```

运行结果：

![](%E8%B7%91Tensorflow%E6%A8%A1%E5%9E%8B%E8%AE%BE%E7%BD%AE%E7%94%A8GPU%E7%9A%84%E4%B8%80%E4%BA%9B%E6%80%BB%E7%BB%93_cv_lz%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2/x-oss-process=image.1.png)

## 四、查看/安装cuda、cudnn版本

1.查看显卡gpu情况

nvidia-smi

2.查看cuda版本

cat /usr/local/cuda/version.txt

3.查看cudnn版本

cat /usr/local/cuda/include/cudnn.h | grep CUDNN\_MAJOR -A 2

4.不同版本的tensorflow-gpu与CUDA对应关系如下表所示:

网址：[https://tensorflow.google.cn/install/source](https://tensorflow.google.cn/install/source)

![](%E8%B7%91Tensorflow%E6%A8%A1%E5%9E%8B%E8%AE%BE%E7%BD%AE%E7%94%A8GPU%E7%9A%84%E4%B8%80%E4%BA%9B%E6%80%BB%E7%BB%93_cv_lz%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2/x-oss-process=image.2.png)

    对于版本号大于1.13的tensorflow-gpu版本，如1.14、1.15和2.0，要安装CUDA10.0，不要安装最新的CUDA10.1，安装后会提示缺少很多库文件，而导致GPU版本的tensorflow无法使用

注意：

（1）确定自己要安装哪个版本的tensorflow-gpu；

（1）根据自己要装的tensorflow-gpu版本确定要下载的CUDA版本；

（2）根据要安装的CUDA版本确定要下载的Cudnn版本。

5.安装tensorflow-gpu

```
pip install tensorflow-gpu==1.14.0
```

6.有用的博客

[https://blog.csdn.net/aaon22357/article/details/82733218?utm\_medium=distribute.pc\_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth\_1-utm\_source=distribute.pc\_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase](https://blog.csdn.net/aaon22357/article/details/82733218?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)

## 五、代码一些问题

## 错误1：No module named 'tensorflow.contrib'

原因：tensorflow 2.0以后没有 tensorflow.contrib，需要降低tensorflow版本问题解决

source activate 环境

conda list

pip install tensorflow==1.14.0

##
错误2：AttributeError: module 'scipy.misc' has no attribute 'imresize'

解决方法：降低scipy的版本

scipy原来版本1.4.1

执行命令pip install scipy==1.2.1

              pip3 install Pillow

解决

## 错误3：

![](%E8%B7%91Tensorflow%E6%A8%A1%E5%9E%8B%E8%AE%BE%E7%BD%AE%E7%94%A8GPU%E7%9A%84%E4%B8%80%E4%BA%9B%E6%80%BB%E7%BB%93_cv_lz%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2/x-oss-process=image.3.jpeg)

原因：conda list终端命令     查看tensorflow版本太高为2.2.0

解决方法：降低tensorflow版本

pip install  tensorflow==1.14.0

重新安装keras

pip install keras==2.2.0

## 错误4：ImportError: libcublas.so.9.0: cannot open shared object file: No such file or directory  (跑yolo3-keras)

## ![](%E8%B7%91Tensorflow%E6%A8%A1%E5%9E%8B%E8%AE%BE%E7%BD%AE%E7%94%A8GPU%E7%9A%84%E4%B8%80%E4%BA%9B%E6%80%BB%E7%BB%93_cv_lz%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2/20200903111438619.png)

**我的环境：**cuda9.0.176  、   cudnn7.3.0 、   tensorflow-gpu1.6.0 、  没有装tensorflow  、Keras2.1.5 、  python3.5.6 (版本都对应好了还是出错)  

**原因：**因为cuda环境变量配置有误

**解决方法:**    执行：

```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/【CUDA版本】/lib64export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-9.0/lib64
```

之后执行：

```
# Pythonimport tensorflow as tfhello = tf.constant('Hello, TensorFlow!')sess = tf.Session()print(sess.run(hello))
```

没有问题了
