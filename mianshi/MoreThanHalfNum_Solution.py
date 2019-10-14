#coding:utf-8

def moreThanHalfNum(lis):
    if not lis:
        return None

    middle = len(lis) // 2
    res_dict = {}
    for num in lis:
        if num in res_dict:
            res_dict[num] += 1
        else:
            res_dict[num] = 1

    # 按value升序
    # [(1, 1), (2, 1), (3, 1)] # 元祖序列
    res_list = sorted(res_dict.items(), key = lambda x: x[1])
#    print "type(res_dict)", type(res_dict)
#    print "res_dict:", res_dict
#    print "res_dict[-1][1]:", res_dict[-1][1]
    if res_list[-1][1] > middle:
        return res_list[-1][0]
    else:
        return None

def moreThanHalfNum2(lis):
    if not lis:
        return None

    lis.sort()
    mid = len(lis) // 2

    count = 0
    for num in lis:
        if num == lis[mid]:
            count += 1
    if count > mid:
        return lis[mid]
    else:
        return None


if __name__ == "__main__":
    l0 = [1, 2, 3] # None
    l1 = [1, 2, 2] # 2
    l2 = [1, 2, 3, 3] # None
    l3 = [1, 3, 3, 3] # 3
    l4 = [4, 4, 1, 2, 4]  # 4

    print moreThanHalfNum(l0)
    print moreThanHalfNum(l1)
    print moreThanHalfNum(l2)
    print moreThanHalfNum(l3)
    print moreThanHalfNum(l4)
    print
    print moreThanHalfNum2(l0)
    print moreThanHalfNum2(l1)
    print moreThanHalfNum2(l2)
    print moreThanHalfNum2(l3)
    print moreThanHalfNum2(l4)
