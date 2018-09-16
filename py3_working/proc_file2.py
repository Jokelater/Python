#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#全局变量和局部变量的使用，在进行进程id的计算
import os
counter = 0
def isNum(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            break
    else:
        print(s)
        global counter
        counter += 1
for i in os.listdir("/proc"):
    isNum(i)
print(counter)