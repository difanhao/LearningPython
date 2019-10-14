#coding:utf-8

# 输出第N大的数
'''
缺点是：使用set方法无法保证去重后的顺序。
但是，可以通过列表中索引（index）的方法保证去重后的顺序不变。
1 li=[1,2,3,4,5,1,2,3]
2 new_li=list(set(li))
3 new_li.sort(key=li.index)
4 print(new_li)
'''
import heapq

def topN(lis, n):
    max_heap = []
    length = len(lis)
    if not lis or n <= 0 or n > length:
        return None

    for ele in lis:
#        ele = -ele
        if len(max_heap) < n:
            heapq.heappush(max_heap, ele)  # 往堆中插入一条新的值
        else:
            heapq.heappushpop(max_heap, ele)  # 顾名思义，将值插入到堆中同时弹出堆中的最小值

#    return map(lambda x: -x, max_heap)
    return max_heap

def topN1(lis, n):
    if not list or n <= 0 or n > len(lis):
        return None

    heapq.heapify(lis) # 小根堆
    print "转换为小根堆(list)", lis

    print len(lis) , n
    while len(lis) != n:
        print heapq.heappop(lis)

    return lis

if __name__ == "__main__":
    l = [2, 1, 9, 9, 2, 4, 7, 6, 3, 3, 1]

    print "原列表:", l
    l1 = list(set(l)) # 去重，注意写法;。
    print "去重后", l1
    l1.sort(key = l.index)
    print "通过列表中索引（index）的方法保证去重后的顺序不变\n", l1
    print

    print "第一种方法："
    n = 3
    max_n = topN(l1, n)
    print type(max_n)
    print "结果列表", max_n
    min_val = min(max_n)
    print "第%d大的元素是%s，索引为%d" % (n, min_val, l.index(min_val))
    print

    print "第二种方法："
    n = 4
    max_n = topN1(l1[:], n) # l[:]不修改原列表
    print "原list没有被修改", l1 # 没有被修改
    print "结果列表", max_n
    min_val = min(max_n)
    print  "第%d大的元素是%s，索引为%d" % (n, min_val, l.index(min_val))
