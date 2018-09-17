#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "cui"

"""copy file

use module to copy file
use os module
Thought:
    导入OS模块，使用其中的方法，创建目录与文件
"""
import os
def mkdir(dir):
    """

    :param dir: 要创建的文件路径
    :return: None
    输入目标路径，然后os模块的mkdir方法会将目标文件夹创建
    """
    os.mkdir(dir)
    print("目录创建成功")

def mkfile(file):
    """

    :param file: 要创建的文件路径
    :return: None
    输入目标路径，然后os模块的 方法将会将文件创建
    """
    os.mknod(file)
    print("文件创建成功")

if __name__ == "__main__":
    #mkdir("/root/aaa")
    mkfile("/root/567.txt")