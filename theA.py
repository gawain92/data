#!/usr/bin/env python
#_*_ coding:utf-8 _*_

name = input("请输入您的用户名：")
password = input("请输入您的密码：")
name = name.lower()
c = 0
while name != 'jack' or password != "123":
    print("输入的账号或者密码错误,请重新输入")
    name = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    c +=1
    if c == 2:
        print("输入错误3次，强制退出")
        break
else:
    print("欢迎登陆")

