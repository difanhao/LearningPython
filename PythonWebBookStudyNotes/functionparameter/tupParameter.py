#coding:utf-8

# * 可以引用元祖，将多个参数组合在一个元祖中

def login(* userpwds):
    username = userpwds[0]
    password = userpwds[1]

    if username == "admin" and password == "admin":
        print "登录成功!"
    else:
        print "登录失败!"

login("admin", "admin")
login("yang", "yang")