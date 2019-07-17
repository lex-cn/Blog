#ThinkPad T440p安装debian之显卡驱动篇<!--{{{--> 

## 获取当前设备的显卡情况
```bash
lspci | grep VGA
```

ThinkPad T440p的显卡设备主要有以下

```bash
00:02.0 VGA compatible controller: Intel Corporation 4th Gen Core Processor Integrated Graphics Controller (rev 06)
02:00.0 VGA compatible controller: NVIDIA Corporation GK208M [GeForce GT 730M] (rev a1)
```

可以看出我们当前的显卡有两块，其中Intel的显卡可以不用管，Linux对Intel显卡的默认
支持非常好，当前的Nvidia显卡核心是GK208M，型号是GT730M，那么我们在软件库中搜索
相关软件包

```bash
sudo apt-get update
apt-cache search GT 730 #此处不要搜索730M
```

搜索结果为

```
nvidia-legacy-304xx-driver - NVIDIA metapackage (304xx legacy version)
nvidia-legacy-304xx-kernel-dkms - NVIDIA binary kernel module DKMS source (304xx legacy version)
nvidia-legacy-304xx-kernel-source - NVIDIA binary kernel module source (304xx legacy version)
xserver-xorg-video-nvidia-legacy-304xx - NVIDIA binary Xorg driver (304xx legacy version)
nvidia-legacy-340xx-driver - NVIDIA metapackage (340xx legacy version)
nvidia-legacy-340xx-kernel-dkms - NVIDIA binary kernel module DKMS source (340xx legacy version)
nvidia-legacy-340xx-kernel-source - NVIDIA binary kernel module source (340xx legacy version)
xserver-xorg-video-nvidia-legacy-340xx - NVIDIA binary Xorg driver (340xx legacy version)
```

这说明现在库中包含你的显卡所要使用的驱动，那么我们可以从库中直接安装。使用库中
的软件的好处是显而易见的。但是我们搞不清到底使用哪种驱动

## 安装

下面安装nvidia-detect，然后运行它
```bash
sudo apt-get install nvidia-detect
nvidia-detect
```
运行结果如下
```
Detected NVIDIA GPUs:
02:00.0 VGA compatible controller [0300]: NVIDIA Corporation GK208M [GeForce GT 730M] [10de:1290] (rev a1)

Checking card:  NVIDIA Corporation GK208M [GeForce GT 730M] (rev a1)
Your card is supported by the default drivers and legacy driver series 340.
It is recommended to install the
    nvidia-driver
package.
```
现在就很明显了，直接安装nvidia-driver即可。

```bash
sudo apt-get install nvidia-driver nvidia-legacy-340xx-driver xserver-xorg-video-nvidia-legacy-340xx 
sudo apt-get install primus bumblebee bumblebee-nvidia
#此处是必须的,否则会出现类似GLX is not supported的问题
```

## 使用显卡

安装完了之后，nvidia显卡默认不起用，所以需要时要用primus包中的optirun启动

比如我要启动0ad这个游戏
```
optirun 0ad
```

## 查看显卡内存使用量

也许你可能想显卡到底启用没，那么可以使用nvidia-smi来查看。比如我玩游戏前，
nvidia-smi的输出如下
```
Sun Oct 30 10:47:49 2016       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 367.44                 Driver Version: 367.44                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GT 730M     Off  | 0000:02:00.0     N/A |                  N/A |
| N/A   53C    P0    N/A /  N/A |      0MiB /   982MiB |     N/A      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID  Type  Process name                               Usage      |
|=============================================================================|
|    0                  Not Supported                                         |
+-----------------------------------------------------------------------------+
```
下面是启动游戏后的结果
```
Sun Oct 30 10:48:44 2016       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 367.44                 Driver Version: 367.44                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GT 730M     Off  | 0000:02:00.0     N/A |                  N/A |
| N/A   56C    P0    N/A /  N/A |     85MiB /   982MiB |     N/A      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID  Type  Process name                               Usage      |
|=============================================================================|
|    0                  Not Supported                                         |
+-----------------------------------------------------------------------------+
```
可以明显看到显卡内存占用增加了85m。另外，请自行删除旧的nouveau程序。

usermod -a -G bumblebee $USER 


注：个人经验之言，仅供参考。

<!--}}}--> 
