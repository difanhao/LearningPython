#coding:utf-8

# apply()函数可以实现调用可变参数列表的功能
# apply(function_name [ , args [ , kwargs]])
# function_name：该参数必需的，表示自定义函数的名称
# args：该参数是可选的，它是一个包含了自定义函数参数的列表或元祖，如果不指定该参数，则表示被执行的函数没有任何参数
# keargs：该参数是可选的，它是一个字典类型的参数，字典中的key值为函数的参数名称，value值为实际参数的值

def login(username, password):
    msg = ""
    if username == "admin" and password == "admin":
        msg = "登录成功"
    else:
        msg = "登录失败"

    return  msg

# 使用apply()实现调用可变参数列表
# 元祖
# apply()函数的元祖参数是有序的，必须与login()函数的形式参数顺序保持一致
print apply(login, ("admin", "admin"))
print apply(login, ("yang", "yang"))

# 字典
def login_kw(** kw):
    print type(kw), kw
    print apply(login, (), kw)

# 间接
login_kw(username = "admin", password = "admin")
# 直接
print apply(login, (), {'username': 'admin', 'password': 'admin'})
print apply(login, (), {'password': 'admin', 'username': 'admin'})  # 字段是无序的

