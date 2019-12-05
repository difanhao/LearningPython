#coding:utf-8

def bubbleSort(lis):
    lenth = len(lis)

    if lenth <= 1:
        return

    for i in range(lenth - 1):
        for j in range(lenth - i - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]


if __name__ == "__main__":
    l = [1, 3, -1, 2, 10, 7, 100, 0]
    bubbleSort(l)
    print l