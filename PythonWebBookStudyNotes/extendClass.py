#coding:utf-8

class Person(object):
    def __init__(self, name): # __init__构造函数参数带self
        self.name = name
        print "父类Person的构造函数,我的名字是", self.name

class Star(Person):
    def __init__(self, name):
        # 调用父类的构造方法，的两种写法
        #Person.__init__(self, name) # 注意后面也有self  !!!!!!!!!!!!!
        super(Star, self).__init__(name) # super写法，扩展性更好


        print "子类Star的构造函数，我的名字是", self.name # 直接写为self.name就好

star = Star("YangFan")
