#coding:utf-8

# 实现一个堆栈
# 后进先出

class MyStack:
    def __init__(self):
        self.__l = []

    def push(self, item):
        '''添加新元素入栈'''
        self.__l.append(item)

    def pop(self):
        '''弹出栈顶元素出栈'''
        if self.__l:
            return self.__l.pop()
        return None

    def peek(self):
        '''返回栈顶元素'''
        if self.__l: # 不为空
            return self.__l[-1]
        return None

    def isEmpty(self):
        return self.__l == [] # 注意，这里不能只写为 return self.__l

    def size(self):
        return len(self.__l)

if __name__  == "__main__":
    # 以下为一些list测试
    '''
    # list为空时，执行pop
    l0 = []
    print l0.pop() # IndexError: pop from empty list
    '''
    # index超界时
    l1 = [1, 2]
    print l1.pop(-1) # 2
    print l1 # [1]
    # print l1.pop(1) # IndexError: pop index out of range

    # 下面开始测试堆栈类
    s = MyStack()
    print "栈大小为", s.size()
    print s.pop()
    print "栈大小为", s.size()
    print "入栈1"
    s.push(1)
    print "栈大小为", s.size()
    print "入栈2"
    s.push(2)
    print "栈大小为", s.size()
    print "栈顶元素为", s.peek()
    print "出栈", s.pop()
    print "栈大小为", s.size()
    print "出栈", s.pop()
    print "栈大小为", s.size()
    print "栈是否为空", s.isEmpty()
    print "为空时，继续出栈", s.pop()


