#coding:utf-8
# 当调用readline方法时，就会前进到下一列，直到文件末尾，返回一个空字符串
f = open("ceshi.py")
print f.readline()
print f.readline()
print f.readline()
print f.readline()
f.close()


print "----------------------"

for readline in open("ceshi.py"):
    print readline