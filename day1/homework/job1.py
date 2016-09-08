#!/usr/bin/env python3

user = 'javier'
passwd = '123456'
black_list = 'black_user'


def login_check(user):
    with open(black_list, "r") as f:
        if user in f.readlines():
            return True
        else:
            return False


def add_black_user(user):
    with open(black_list, "a") as f:
        f.writelines(user)


username = input('请输入用户名：')
password = input('请输入密码：')
