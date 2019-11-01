#coding:utf-8
'''
zip()迭代是把两个序列“压缩”在一起，然后返回一个元祖的列表；
enumerate()返回索引、值对儿
'''

names = ["yang", "zhang", "shi"]  # 序列长度不同，没关系
ages = ["31", "32"]

i = 0
for name, age in zip(names, ages):
    i += 1
    print name, "的年龄是", age

print "循环%d次\n" % i
print "---------"

for t in enumerate(names):
    print type(t), t

for index, name in enumerate(names):
    print index, name


