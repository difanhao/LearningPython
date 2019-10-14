#coding:utf-8

def binarySearch(list, num):
    low = 0
    high = len(list) - 1

    i = 0
    while low <= high:
        i += 1
        middle = (high + low) / 2

        print "low=%d, high=%d, middle=%d" % (low, high, middle)

        guess = list[middle]
        if guess == num:
            print "循环%d次" % i
            return middle
        elif guess < num:
            low = middle + 1
        else:
            high = middle - 1
    print "循环%d次" % i
    return None

l = range(10)
for i in l:
    print "本次查找", str(i)
    r = binarySearch(l, i)
    if  r != None:
        print "找到了，索引是%s\n" % str(r)
    else:
        print "没找到!"