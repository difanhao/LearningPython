#coding:utf-8
import time

# 但会当前时间戳
myTime = time.time()
print type(myTime)
print "当前时间戳为:", myTime
print

# time.localtime()返回时间元祖
localtime = time.localtime()
print type(localtime)
print localtime
print

# time.strptime(string[, format]) 函数接收以时间元组，并返回以可读字符串表示的当地时间，
# 格式由参数format决定。
print "当前时间为:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())