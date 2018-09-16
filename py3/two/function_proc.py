#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#查看输入文件中包含的纯数字的文件数

import os
counter = 0
def isNum(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            print("is not")
    else:
        print(s)
        global counter
        counter += 1
for z in os.listdir("/proc"):
    isNum(z)
print(counter)