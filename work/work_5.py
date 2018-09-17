#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "cui"

"""build password

make a password 
"""

import string,random

def mkPasswd(amount=8):
    "默认能产生8位数的密码，可以通过输入参数来确定产生密码的位数，但不能少于8"

    amount = int(amount)
    password = ""
    if amount<8 :
        print("低于8位数的密码安全性较低，本方法不支持产生低于8位数的密码")
        return False
    for i in range(amount):
        password=making(password)
    return password

def making(str1):
    a = string.ascii_letters + string.digits
    return str1 + str(random.choice(a))

if __name__ == "__main__":
    print(mkPasswd(14))