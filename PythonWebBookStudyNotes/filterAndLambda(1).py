#coding:utf-8
# p105例题
import random

l = []

for i in range(10):
    l.append(random.randint(1000, 9999))

print "随机从1000-9999中获取的10个数为：", l
print "其中，偶数有：", filter(lambda x: x % 2 == 0, l)
print "其中，奇数有：", filter(lambda x: x % 2 != 0, l)