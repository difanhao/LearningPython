#coding:utf-8

# list.sort()列表排序
# list.reverse()方法将  列表！ 反向存放
# 它们改变了原列表！！！！！！！，但不返回值！！！！！！！！！！

#sort 与 sorted 区别：
#sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
#list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，
# 而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

lis = [1, 3, 2]
lis.reverse()
print lis

lis.sort()
print lis
lis.sort(reverse = True)
print lis
print

tup = (1, 3, 2)
str = "132"
tup = sorted(tup)
str = sorted(str)
print tup
print str  # ['1', '2', '3']
print

l = [-1, -2]
l_sorted = sorted(l) # 保留原列表
print l_sorted
print l
print

l1=[('b',3),('a',2),('c',5),('d',4)]
print sorted(l1, cmp=lambda x,y:cmp(x[1], y[1]))   # 利用cmp函数
print sorted(l1, key = lambda x: x[0])  # 利用key
print sorted(l1, key=lambda x: x[1])               # 利用key
print

dict = {"a": 9, "world": 10, "z": 8, "hello": 12}
print sorted(dict.items(), key = lambda x: x[0]) # 按key值升序
print sorted(dict.items(), key = lambda x: x[1]) # 按value值升序
