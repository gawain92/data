#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "cui"

"""Introduction Module

os:可以用于执行一些liunx中的方法
sys:系统模块，内有系统常用的方法
random:随机数模块，可以用于随机获取一个字符串中的随机一个字符，或者是获取列表或元祖中的随机一个下标对应的值
keyword:关键字模块，可以使用里面的iskeyword来判断是否是关键字
string:字符类型的模块，里面有字符类型的操作方法
py_compile:用于编译Python脚本，编译完的Python脚本后缀为pyc，在3版本的Python中没有pyo
"""
import os,sys
import random,keyword,string
import py_compile

def useOs():
    """
    python3 work_3.py sdir
    1.获取系统信息
    2.获取传参路径下面所有的文件和文件夹名称，以列表的形式
    返回(使用了sys的argv方法，可以当文件在liunx中执行时候，
    此方法可以获取到位置参数，将位置参数传参给该方法)
    :return: 返回位置参数传参路径下的所有文件和文件夹名称，以列表形式
    """
    print(os.uname())
    return os.listdir(sys.argv[1])

def useSys():
    "输出Python搜索模块的路径，可在其后使用.append()方法追加其他路径"
    print(sys.path)
def useRandom():
    "使用随机数模块，随机获取一个字符串中的一个字符或者一个元祖或一个列表中的一个下标对应的值"
    print(random.choices("abcdefg"))
    print(random.choices(["abcdefg","hijkopq",1,2,3,("tom","jack","li")]))
    print(random.choices(("tom", "jack", "li")))

def useKeyword(str1):
    "判断一个词是否是关键字"
    if keyword.iskeyword(str1):
        print("YES")
    else:
        print("不是关键字")
def usePy_compile(sdir):
    "将一个Python脚本进行编译"
    py_compile.compile(sdir)
def useString():
    "可以获取所有的大小写字母以及数字"
    print(string.ascii_letters)
    print(string.digits)

if __name__ == "__main__":
    #useOs()
    useSys()
    useRandom()
    useKeyword("False")
    #usePy_compile("/root/PythonProject/day2_3/theDay3.py")
    useString()