#coding:utf-8

l = ["Who", "are", "you", "?"]

for i in l:
    print i
print

iter_l = iter(l)
for i in iter_l:
    print i
#print iter_l.next() # StopIteration异常
print

iter_ll = iter(l) # 创建新迭代器，从头开始
while True:
    i = next(iter_ll, "end")
    print i
    if i == "end":
        break

print iter_ll.next() # StopIteration异常