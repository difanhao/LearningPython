#coding:utf-8
'''
tupleArg前面“*”表示这个参数是一个元组参数，从程序的输出可以看出，默认值为()；
dicrtArg前面有“**”表示这个字典参数(键值对参数)。
可以把tupleArg、dictArg看成两个默认参数。
多余的非关键字参数，函数调用时被放在元组参数tupleArg中；多余的关键字参数，函数调用时被放字典参数dictArg中
(1)如代码:fun(123, l, dict)
　　元组对象前面如果不带“*”、字典对象如果前面不带“**”，则作为普通的对象传递参数。
　　多余的普通参数，在foo(123,myList,myDict)中，123赋给参数arg1，myList赋给参数arg2，多余的参数myDict默认为元组赋给myList。

(2)如代码最后一行;fun(123, rt=123, *l, **dict)
　　　参数中如果使用“*”元组参数或者“**”字典参数，这两种参数应该放在参数列表最后。并且“*”元组参数位于“**”字典参数之前。
　　　关键字参数rt=123,因为函数foo(arg1,arg2="OK",*tupleArg,**dictArg)中没有rt参数，所以最后也归到字典参数中。
'''

def fun(arg1, arg2="OK", *tupleArg, **dictArg):
    print "arg1 = ", arg1
    print "arg2 = ", arg2

    for i, ele in enumerate(tupleArg):
        print "tupleArg %d --> %s" % (i, ele)

    for key in dictArg:
        print "dictArg %s --> %s" % (key, dictArg[key])

l = ["ele0", "ele1"]
dict = {"name": "yang", "age": "31"}
fun("formal_args", arg2="argSecond", a=1)
print "*" * 40

fun(123, l, dict)
print "*" * 40

fun(123, rt=123, *l, **dict)

