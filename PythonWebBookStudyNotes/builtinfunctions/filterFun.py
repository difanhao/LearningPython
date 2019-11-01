#coding:utf-8

# filter()函数可以对序列做过滤处理
# filter(function_name, sequence)
# function_name：该参数是必需的，它是自定义函数，在函数function_name()中定义过滤规则
# 如果function_name()返回值为None，则表示sequence序列中的每一项都为True，从而返回左右的序列元素
# sequence：该参数也是必需的，表示需要过滤的序列

# filter()函数的返回值由function_name()函数的返回值决定，function_name()函数返回所有为True的过滤项组成的序列，返回值的类型与参数sequence的类型相同


# 书中例题
def validate(usernames):
    length = len(usernames)
    if length > 4 and length < 12:
        return usernames

# 调用filter()，过滤validate()函数中的元祖参数
print filter(validate, ("admin", "yangfan", "mxl", "adm", "wanglili"))

print "-----------------"

# p105例题
import random

l = []

for i in range(10):
    l.append(random.randint(1000, 9999))

print "随机从1000-9999中获取的10个数为：", l
print "其中，偶数有：", filter(lambda x: x % 2 == 0, l)
print "其中，奇数有：", filter(lambda x: x % 2 != 0, l)