#coding:utf-8

#洗牌算法，乱排
import random

def myShuffle(lis):
    result = []
    while lis:
        r = random.randrange(0, len(lis))
        result.append(lis.pop(r))
    return result

def myShuffle2(lis):
    for index in range(len(lis) - 1, -1, -1):
        print "index:", index
        r = random.randrange(0, index + 1)
        print "r:", r
        lis[index], lis[r] = lis[r], lis[index]

if __name__ == "__main__":
    '''
    # 打乱一个排好序的list对象alist？
    alist = range(10)
    random.shuffle(alist)
    print alist
    '''
    l = range(1, 6)
    r = myShuffle(l)
    print r
    print l # []!!!!!!!!!!!!!!!!
    print

    l = range(1, 6)
    myShuffle2(l)
    print l