#coding:utf-8

def sum_of_two(arr,target):
    dic = {}
    for i,x in enumerate(arr):
        j = dic.get(target-x,-1)
        if j != -1:
            return((j,i))
        else:
            dic[x] = i
    return([])

arr = [2,7,4,9]
target = 6
print(sum_of_two(arr,target))
