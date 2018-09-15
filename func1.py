#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "cui"

def jia(x,y):
    return "%s + %s = %s" %(x,y,x+y)
def jian(x,y):
    return "%s - %s = %s" %(x,y,x-y)
def chen(x,y):
    return "%s * %s = %s" %(x,y,x*y)
def chu(x,y):
    return "%s / %s = %.2f" %(x,y,x/y)

try:
    a = int("a")
    import xxxx
except ValueError as c:
    print("强转失败，请重新输入正确的参数\n%s" %c)
except ModuleNotFoundError as d:
    print("没有此模块，请输入正确的模块\n%s" %d)
