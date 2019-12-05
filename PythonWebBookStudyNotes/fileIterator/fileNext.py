#coding:utf-8
# 当调用next()方法时，执行到文件末尾，不会返回空字符串，而是引发内置的 StopIteration异常
f = open("ceshi.py")
print f.next()
print f.next()
print f.next()
#print f.next()  # StopIterations
f.close()

print "----------------------"

for next in open("ceshi.py"):
    print next