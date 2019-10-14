#coding:utf-8
a = 1
b  = [2, 3]
c = 4

def fun():
    print "in fun()"
    a = 3
    print a

    b[0] = 10
    print b

    global c
    c = 5
    print c



print a
print b
print c
print

fun()
print

print a
print b
print c
print