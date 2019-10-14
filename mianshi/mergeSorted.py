#coding:utf-8

def merge_sorted_array(a,b):
    c = []
    i,j = 0,0

    while True:
        if i==len(a):
            c.extend(b[j:])
            return(c)
        elif j==len(b):
            c.extend(a[i:])
            return(c)
        else:
            if a[i]<b[j]:
                c.append(a[i])
                i=i+1
            else:
                c.append(b[j])
                j=j+1

print(merge_sorted_array([1,2,6,8],[2,4,7,10]))
