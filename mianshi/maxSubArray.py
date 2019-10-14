#coding:utf-8

def max_sub_array(arr):
    n = len(arr)
    maxi,maxall = arr[0],arr[0]
    for i in range(1,n):
        maxi = max(arr[i],maxi + arr[i])
        maxall = max(maxall,maxi)
    return(maxall)

print(max_sub_array([1,5,-10,2,5,-3,2,6,-3,1]))

