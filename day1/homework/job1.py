#!/usr/bin/env python3

black_list = 'black_user'
count = 0
user_db = {
    'javier': '123456',
    'zjw': '123'
}


def login_check(user):
    with open(black_list, "r") as f:
        if user in f.readlines():
            return True
        else:
            return False


def add_black_user(user):
    with open(black_list, "a") as f:
        f.writelines(user)


while count < 3:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if login_check(username):
        print('账户已被锁定！')
        break
    elif username in user_db and password == user_db[username]:
        print('登陆成功！')
        break
    else:
        print('账户或密码错误！')
        count += 1
else:
    print('尝试次数过多！')
    add_black_user(username)