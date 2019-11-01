#coding:utf-8

# map()函数对 多个 序列中的 每个元素执行相同的操作，并返回一个与输入序列长度相同的列表
# map(function_name, sequence[ , sequence, ...])
# 参数sequence的个数可以是多个
# map()函数对 多个 序列中的 每个元素执行相同的操作，并返回一个与输入序列长度相同的列表
# 如果每个序列的长度不限共，则在长度短的序列后补充None，再进行计算
# map()返回都是list

print map(lambda x: x ** 2, (0, 1, 2, 3, 4, 5)), type(map(lambda x: x ** 2, (0, 1, 2, 3, 4, 5)))  # <type 'list'>


print map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])

#长度不同，短的补None
print map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6, 7])  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'


