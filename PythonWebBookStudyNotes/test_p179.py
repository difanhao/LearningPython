#coding:utf-8
import re

l = [1, 2, 3]
a, b, c = l # a, b = l 报错
print a, b, c

while True:
    num = raw_input("请输入您的电话号码: ")
    r = re.compile(r"^\d{4}-[1-9]\d{7}$")
    if re.match(r, num):
        print "电话号码验证通过"
        print type(re.split("-", num))
        direct_num, tel_num = re.split("-", num)
        print "区号为：", direct_num
        print "号码为：", tel_num
        break
    else:
        print "电话号码验证失败!"

