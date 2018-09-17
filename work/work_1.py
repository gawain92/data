#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "cui"

"""copy file

it is use to copy file
python version: 3.6.6
Thought:
    先将IO流打开，通过函数传参的方式给定源路径，对源文件进行读取，然后通
    过循环行读取的列表，将读取到的内容追加写入到给定的目标路径，使用的是
    with的方式，其会自动在使用完毕后将IO流关闭
"""
def copyFile(sdir,desdir):
    """sdir is source directory
    desdir id destination directory
    copy sdir to desdir"""
    with open(sdir,"r") as f1:
        for co in f1.readlines():
            with open(desdir,"a")  as f2:
                f2.write(co)

    print("成功将%s复制到%s" %(sdir,desdir))

if __name__ == "__main__":
    copyFile("/root/123.txt","/home/cui/456.txt")