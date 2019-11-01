#coding:utf-8

#reduce()函数可以实现连续处理功能
# reduce(function_name, sequence[ , initial])
# function_name、sequence：这两个参数是必需的
# initial：该参数是可选的，如果指定了该参数的值，则initial所指定的值将首先被传入function_name()函数中进行计算
# 如果sequence参数的值为空，则对inittal所指定的值进行处理

def operat(x, y):
    return x * y

# 使用reduce()函数，对序列中的每一项进行计算，最后将计算结果返回
print reduce(operat, (1, 2, 3, 4))  # 1 * 2 * 3 * 4
print reduce(operat, (1, 2, 3, 4), 5)  # 5 * 1 * 2 * 3 * 4
print reduce(operat, (), 5)  # 5
print reduce(lambda x, y: x + y, [1, 2, 3])
