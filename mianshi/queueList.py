#coding:utf-8

class MyQueue(object):
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        '''入队'''
        self.__list.append(item)

    def dequeue(self):
        '''出队'''
        if self.__list:
            return self.__list.pop(0)
        return None

    def isEmpty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

if __name__ == "__main__":
    q = MyQueue()

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

