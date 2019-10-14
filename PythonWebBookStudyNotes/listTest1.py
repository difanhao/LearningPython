#coding:utf-8
# list添加元素,append insert
# 删除元素 remove del pop


print "添加:"
l = [1, 2, 3]
l.append(4)
print l
l.insert(0, 0)
print l
l.insert(100, 4)
print l

print "删除:"
l.remove(4) #删除第一个4，找不到4跑出ValueErroe
print l
del l[0]
print l
l.pop()
print l
# pop是唯一一个既能修改列表又能返回元素值（除了None）的列表操作方法
print l.pop(1)
print l