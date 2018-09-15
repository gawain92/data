#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "cui"

import random

all_choice = ['石头','剪刀','布']
win_list = ['石头','剪刀'],['剪刀','布'],['布','石头']
prompt = """(0)石头
(1)剪刀
(2)布
请选择{0|1|2}:"""

pwin = 0
cwin = 0
while pwin < 2 and cwin < 2:
    index = input(prompt)
    while not (index == '0' or index == '1' or index == '2'):
        print("输入错误，请输入正确的选项{0|1|2|}")
        index = input(prompt)
    index = int(index)
    player = all_choice[index]
    compute = random.choice(all_choice)

    print("player:%s,compute:%s" %(player,compute))
    if player == compute:
        print("\033[25;33;1m平局\033[0m")
    elif [player,compute] in win_list:
        print("你赢了")
        pwin += 1
    else:
        print("你输了")
        cwin += 1

if pwin == 2:
    print("win")
else:
    print("lose")