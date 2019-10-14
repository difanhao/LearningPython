#coding:utf-8

# 元祖不可变序列，不可对元素赋值

# 创建元祖，可以这么写
tup = 1, 2, 3
print type(tup), tup
print

# 元祖只有一个元素时，必须写逗号，不然会解释为表达式
myTup0 = (1)
myTup1 = (1,)
print type(myTup0), myTup0
print type(myTup1), myTup1
print

# 元祖的打包和解包
t = (1, 2, 3) # 打包
a, b, c = t # 解包
print a, b, c
print

