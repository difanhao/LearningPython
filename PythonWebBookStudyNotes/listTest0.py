#coding:utf-8
# 切片，5-2=3，就是3个元素
# extend()不会创建新的list
# sort()只会修改原有列表，不会创建新列表，返回为Nnoe
# reverse()反向排列，也是只会修改原列表，返回为Nnoe
l = range(6)
print l
print "l[2:5]:", l[2:5]
print "l[2:-2]:", l[2:-2]
print

l0 = [1, 2, 3]
l1 = [4, 5]
print "extend之前，内存值，l0 = %s, l1 = %s" % (id(l0), id(l1))
l0.extend(l1)
print "extend之后，内存值，l0 = %s, l1 = %s" % (id(l0), id(l1))
print

l2 = [6, 7, 8]
l3 = [9, 10]
print "+之前，内存值，l2 = %s, l3 = %s" % (id(l2), id(l3))
l2 += l3
print "+之后，内存值，l2 = %s, l3 = %s" % (id(l2), id(l3))
print

l4 = [2, 1, 3]
print "sort之前，内存值，l4 = %s" % id(l4)
l5 = l4.sort()
print "sort之后，内存值，l4 = %s" % id(l4)
print "sort之后，l4 = %s，l5 = %s" % (l4, l5)
# 倒叙排列
l4.sort(reverse=True)
print "倒叙之后，l4 = %s" % l4
print

l6 = [2, 1, 3, 0]
print l6.reverse()
print l6