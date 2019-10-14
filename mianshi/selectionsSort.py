#coding:utf-8

def selectionSort(lis):
    lenth = len(lis)

    if lenth <= 1:
        return

    for i in range(lenth - 1):
        min_index = i
        min_val = lis[min_index]

        for j in range(i + 1, lenth):
            if lis[j] < min_val:
                min_val = lis[j]
                min_index = j

        if min_index != i:
            lis[i], lis[min_index] = lis[min_index], lis[i]

if __name__ == "__main__":
    l = [1, 3, -1, 2, 10, 7, 100, 0]
    selectionSort(l)
    print l

    # 测试range错误边界，是否报错 -- 不报错
    for a in range(9, 10):
        print a
    for a in range(9, 9):
        print a
    for a in range(9, 8):
        print a