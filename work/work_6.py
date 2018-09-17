#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "cui"
""""

抱歉，最后一个开始敲的时候忘记录视频了，因为9点15分要上交作业，来不及重新写，只能将其效果展示
"""
def show():
    #该功能是打印菜单目录
    print("""
    1)菜单1
    2）菜单2
    3）菜单3
    4）退出菜单
    """)
def caidan1():
    #如果选择了1，调用此方法，执行菜单1的功能
    print("执行菜单1")
def caidan2():
    # 如果选择了2，调用此方法，执行菜单2的功能
    print("执行菜单2")
def caidan3():
    # 如果选择了3，调用此方法，执行菜单3的功能
    print("执行菜单3")
def carte():
    end = True
    while end:
        show()
        choose = input("请选择您要使用的功能：")
        if choose == "1":
            caidan1()
        elif choose == "2":
            caidan2()
        elif choose == "3":
            caidan3()
        elif choose == "4":
            end =False
            print("感谢您的使用！再见")
        else:
            print("您的输入有误，请输入正确的选项{1|2|3|4}")

if __name__ == "__main__":
    carte()