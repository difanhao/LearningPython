#coding:utf-8

# ** 可以引用一个字典作为参数

def login(** userpwds): # userpwds: {'username': 'admin', 'password': 'admin'}
    username = ""
    password = ""

    for key in userpwds.keys():
        if key == "username":
            username = userpwds[key]
        if key == "password":
            password = userpwds[key]

    if username == "admin" and password == "admin":
        print "登录成功!"
    else:
        print "登录失败!"

login(username = "admin", password = "admin")
