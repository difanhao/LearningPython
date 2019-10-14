#coding:utf-8

def quickSort(lis):
    lenth = len(lis) # 变量名不能是len
    if lenth <= 1: # <=1
        return lis

    mid_val = lis[lenth // 2]

#    print type(x for x in lis if x < mid_val) # <type 'generator'>
#    print type([x for x in lis if x < mid_val]) # <type 'list'>

    left = [x for x in lis if x < mid_val] # 没有:，记着写if
    left = [x for x in lis if x < mid_val]
    middle = [x for x in lis if  x == mid_val]
    right = [x for x in lis if x > mid_val]

    return quickSort(left) + middle + quickSort(right)

if __name__ == "__main__":
    l = [1, 3, -1, 2, 10, 7, 100, 0]
    print quickSort(l)