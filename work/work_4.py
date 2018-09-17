#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "cui"

"""import

import module
介绍如何去导入模块
"""
from work import work_2
#导入模块时，可以使用form 包 import 模块的方式
#work_2.mkdir("/home/bb")
import sys
sys.path.append("/project/first/work")
# print(sys.path)
import work_2
# work_2.mkdir("/home/ccc")
#将项目文件做成包的方式是，在项目文件目录里创建一个__init__.py文件
import work.work_3
work.work_3.useString()

