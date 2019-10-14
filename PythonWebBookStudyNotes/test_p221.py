#coding:utf-8

class Animal(object):
    def __init__(self, name):
        self.name = name
        print "我的名字叫:", self.name

class Chicken(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def eated(self):
        print "这只火鸡已经被吃了"

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def eated(self):
        print "这狗肉已经被吃了"

class Human(object):
    def eat(self, anaimal):
        anaimal.eated()


if __name__ == "__main__":
    c = Chicken("火鸡")
    d = Dog("单身狗")

    p = Human()
    p.eat(c)
    p.eat(d)