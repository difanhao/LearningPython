#coding:utf-8

def longest_substr(s):
    dic = {}
    start,maxlen,substr = 0,0,""

    for i,x in enumerate(s):
        if x in dic:
            start = max(dic[x]+1,start)
            dic[x] = i
        else:
            dic[x] = i

        if i-start+1>maxlen:
            maxlen = i-start+1
            substr = s[start:i+1]
    return(substr)

print(longest_substr("abcbefgf"))
print(longest_substr("abcdef"))
print(longest_substr("abbcddefh"))
