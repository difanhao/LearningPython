#coding:utf-

# 用栈实现队列
# 初始化两个空的列表作为栈
# 所有的push都放到stack1中
# 所有的pop都从stack2中取（list的pop默认弹出最后一个元素）
# 对pop操作做判断，如果stack2为空就先把stack1中的元素倒入到stack2中，
# 注意是“倒”，这样就可以保证stack2的最后一个元素一定是目前元素中最先进入到stack1的；
# 如果stack2不为空（从stack1倒进stack2的），就直接从stack2中pop出来；

class StackQueue(object):
    def __init__(self):  # 是__init__啊！！不是__init，别忘了后面的__
        self.__stack1 = []
        self.__stack2 = []

    def enqueue(self, item):
        self.__stack1.append(item)

    # 注意写法
    def dequeue(self):
        if self.__stack2:
            return self.__stack2.pop()
        elif self.__stack1:
            while self.__stack1:
                self.__stack2.append(self.__stack1.pop())
            return self.__stack2.pop()
        else:
            return None

    def isEmpty(self):
        return self.__stack1 == [] and self.__stack2 == []

    def size(self):
        return len(self.__stack1) + len(self.__stack2)

if __name__ == "__main__":
    q = StackQueue()

    print "队列大小为", q.size()
    print "出队列", q.dequeue()
    print "队列大小为", q.size()

    print "入队列1"
    q.enqueue(1)
    print "队列大小为", q.size()
    print "入队列2"
    q.enqueue(2)
    print "队列大小为", q.size()

    print "出队列", q.dequeue()
    print "队列大小为", q.size()
    print "出队列", q.dequeue()
    print "队列大小为", q.size()

    print "队列是否为空", q.isEmpty()
    print "为空时，继续出队列", q.dequeue()

    print "入队列3、4"
    q.enqueue(3)
    q.enqueue(4)
    print "队列大小为", q.size(),"此时stac1长度为2，stack2为0"
    print "队列是否为空", q.isEmpty()
    print "出队列", q.dequeue()
    print "入队列5，此时stack1、stack2长度均为1"
    q.enqueue(5)
    print "队列大小为", q.size()
    print "队列是否为空", q.isEmpty()
    print "出队列", q.dequeue()
    print "队列大小为", q.size()
    print "队列是否为空", q.isEmpty()
    print "出队列", q.dequeue()
    print "队列大小为", q.size()
    print "队列是否为空", q.isEmpty()




