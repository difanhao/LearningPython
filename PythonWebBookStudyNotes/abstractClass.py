#coding:utf-8
# 模拟抽象类 p205

def abstract():
    raise NotImplementedError("abstract")

# 如果没有继承object，即class Person(object)
# 下面子类中调用父类__init__方法，不能用super(Star, self).__init__()写法
# 只能用 Person.__init__(self)写法!因为是旧式类 P211
class Person: # 没有继承，不用写括号
    def __init__(self):
        if self.__class__ is Person:
            abstract()

class Star(Person):
    def __init__(self):
        #super(Star, self).__init__()# 或者Person.__init__
        Person.__init__(self)

        print "我是大明星"

star = Star()
person = Person()
