#coding:utf-8

def insertionSort(lis):
    if len(lis) <= 1:
        return

    for i in range(len(lis)):
        pre_index = i - 1
        current = lis[i]

        while pre_index >= 0 and lis[pre_index] > current:
            lis[pre_index + 1] = lis[pre_index]
            pre_index -= 1
            lis[pre_index + 1] = current

l = [1, 3, -1, 2, 10, 7, 100, 0]
insertionSort(l)
print l
