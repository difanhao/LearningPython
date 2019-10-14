#coding:utf-8

'''
判断闰年，测试两种写法，是否都OK：
1： (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) -- 书中P90例题
2： year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) -- calendar.isleap源码
ps：写法1，去掉()是一样的，因为，运算符优先级，算术运算符 > 关系运算符 > 逻辑运算符
'''

# 首先，结合判定表，比对calendar.isleap源码和书中例题的表达式，发现8种结果中，仅有2种结果不同
# 对这两种结果进行测试：0 1 1、0 0 1，发现不存在这种年份。。。
# 可以初步判定，两种写法都行
for year in range(5001):
    if year % 4 != 0 and year % 100 != 0 and year % 400 == 0:
        print "存在这种年份:", year
    if year % 4 != 0 and year % 100 == 0 and year % 400 == 0:
        print "存在这种年份:", year


# 然后，为了进一步证实判断，自编一个myIsLeap方法（与书中一致），与源码比对
import calendar

def myIsLeap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

for year in range(5001):
    if calendar.isleap(year) != myIsLeap(year):
        print "存在这种年份:", year