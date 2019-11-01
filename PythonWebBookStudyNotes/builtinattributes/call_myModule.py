#coding:utf-8

# 由于该模块没有定义文档字符串，所有输出为None

import myModule

print __doc__

class MyClass:
    "MyClass类的描述"
    def printHello(self):
        "printHello()方法用于打印 Hello World"
        print "Hell0 World"

print MyClass.__doc__
print MyClass.printHello.__doc__  # 注意是方法名，不带()