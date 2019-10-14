#coding:utf-8

# filter() 序列什么类型，返回就是啥类型
print filter(lambda x: x % 2 == 0, range(10))
print type(filter(lambda x: x % 2 == 0, range(10)))# <type 'list'>
print type(filter(lambda x: x % 2 == 0, (1, 2, 3, 4)))# <type 'tuple'>

print reduce(lambda x, y: x + y, range(10))

# map()返回都是list
print map(lambda x: x ** 2, (0, 1, 2, 3, 4, 5))
print type(map(lambda x: x ** 2, (0, 1, 2, 3, 4, 5))) # <type 'list'>

print map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]) #长度不同，短的补None
