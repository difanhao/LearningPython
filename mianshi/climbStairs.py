#coding:utf-8

def climb_stairs(n):
    if n==1:
        return 1
    if n==2:
        return 2
    a,b = 1,2
    i = 3
    while i<=n:
        a,b = b,a+b
        i +=1
    return b

print(climb_stairs(10))
