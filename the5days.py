#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "cui"
def showCpuCores():
    "查看CPU的核数"
    with open("/proc/cpuinfo",'r') as f1:
        for i in f1:
            if i.startswith("cpu cores"):
                print(i)

def showMeminfo():
    with open("/proc/meminfo","r") as f2:
        for i in f2:
            if i.startswith("MemTotal:"):
                a = int(i.split()[1])
            if i.startswith("MemFree:"):
                b = int(i.split()[1])
                c = a - b
                break

    print("内存的使用率为%.2f%%,剩余大小为%.1fM" %(c/a*100,b/1024))

def copyFileTo():
    "将一个文件拷贝到另一个地址"
    s_file = "/root/123.txt"
    d_file = "/home/321.txt"

    with open(s_file,'r') as f3:
        for i in f3:
            with open(d_file,"a") as f4:
                f4.write(i)
