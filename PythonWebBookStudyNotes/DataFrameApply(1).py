#coding:utf-8

# 下面的例子是DataFrame中apply的用法
# 学习资料 https://www.cnblogs.com/IvyWong/p/9203981.html

# 函数应用和映射
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['utah', 'ohio', 'texas', 'oregon'])
print(df)
print

# 将函数应用到由各列或行形成的一维数组上。DataFrame的apply方法可以实现此功能
f = lambda x: x.max() - x.min()
# 默认情况下会以列为单位，分别对列应用函数
t1 = df.apply(f)
print(t1)
print
t2 = df.apply(f, axis=1)
print(t2)
print

# 除标量外，传递给apply的函数还可以返回由多个值组成的Series
def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])


t3 = df.apply(f)
# 从运行的结果可以看出，按列调用的顺序，调用函数运行的结果在右边依次追加
print(t3)

"""
            b         d         e
min -0.896774 -2.238288 -0.662676
max  0.701109  1.974801  0.738890
"""

# 元素级的python函数，将函数应用到每一个元素
# 将DataFrame中的各个浮点值保留两位小数
f = lambda x: '%.2f' % x
t3 = df.applymap(f)
print(t3)
"""
            b      d      e
utah    -0.67   1.97   0.74
ohio    -0.90  -0.79   0.47
texas    0.04   0.89  -0.66
oregon   0.70  -2.24  -0.15
"""

# 注意，之所以这里用map,是因为Series有一个元素级函数的map方法。而dataframe只有applymap。
t4 = df['e'].map(f)
print(t4)

"""
utah     0.74
ohio     0.47
texas   -0.66
oregon  -0.15
"""
