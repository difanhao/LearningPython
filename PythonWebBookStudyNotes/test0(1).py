#coding:utf-8

'''
幂运算；
其他的赋值写法；
一些值在作为布尔表达式时，被解析为False
'''

r = 1.5
c = 2 * 3.14 * r
s = 3.14 * (r**2)
print c, s
print ""

x = y = z = 1
print x, y, z
i, j = 2, 3
print i, j
print ""

print True == 1
print False == 0

print bool(None)
print bool("")
print bool(())
print bool([])
print bool({})
print ""