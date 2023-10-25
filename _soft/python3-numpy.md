---
name : numpy总结
---




```python
import numpy as np

m1 = np.arange(10).reshape(2, 5)

m1.T
m1.transpose()     # 矩阵转置
m1.reshape(5,2)    # 重置

m1.dot(m2)    # 乘法
m1*m2         # 不是矩阵乘法，而是按元素乘积。

np.linalg.inv(m3) 
np.linalg.pinv(m3) # 矩阵的逆与伪逆

m3.dot(linalg.inv(m3))  # 单位矩阵

np.eye(n)    #  函数来创建一个N×N大小的单位矩阵。

np.linalg.qr(m3)    #  QR分解
np.linalg.det(m3)    # 行列式

np.linalg.eig(m3)    # 特征值和特征向量
np.linalg.svd(m3)    # 奇异值分解

np.diag(m3)         # 对角线
np.trace(m3)    #  迹

```
##  numpy 求解线性标量方程组  `np.linalg.solve`

求解

$$ 2x + 6y = 6, 5x + 3y = -9  $$

```python
coeffs = np.array([[2, 6], [5, 3]])
depvars = np.array([6, -9])
solution = np.linalg.solve(coeffs, depvars)
```

##  numpy 的矢量化

np.meshgrid()函数



## numpy 常见错误

Np.nanstd()函数的返回值为nan

这种情况是由于所计算的序列当中出现以下几种情况

There are three circumstances where `np.nanstd` might return _NaN_:

1.  If the input is empty 所输入的序列为空
2.  If all of the elements in the input are `NaN` 输入的序列元素全部为nan值
3.  If one of the elements is either positive or negative infinity. To understand why this happens, remember that the formula for standard deviation is：
    $$\delta = \sqrt{\frac{1}{N} \sum^{N}_{i=1}(x-\mu)^2}, where\ \mu=\frac{1}{N}\sum^N_{i=1} x_i$$

**参考资料**

- [python - What could cause numpy.nanstd() to return nan? - Stack Overflow](https://stackoverflow.com/questions/28954429/what-could-cause-numpy-nanstd-to-return-nan)
- [python - Pandas Standard Deviation returns NaN - Stack Overflow](https://stackoverflow.com/questions/32130954/pandas-standard-deviation-returns-nan)

