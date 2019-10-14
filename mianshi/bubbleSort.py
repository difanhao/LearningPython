#coding:utf-8

def bubbleSort(lis):
    lenth = len(lis)

    if lenth <= 1:
        return

    for i in range(1, lenth):
        for j in range(0, lenth - i):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]


if __name__ == "__main__":
    l = [1, 3, -1, 2, 10, 7, 100, 0]
    #l = [100, -1, 2]
    bubbleSort(l)
    print l