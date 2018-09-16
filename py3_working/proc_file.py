#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#查看文件中包含的文件中纯数字的文件的数目，查看proc目录中的进程id

import os
#计数器，计算有多个个进程id文件
counter = 0
def isNum(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            return False
    else:
        #打印是数字的文件的名字：就是进程id
        print(s)
        return True
#for 循环遍历proc目录中的所有文件，当作参数传给isNum函数
for i in os.listdir("/proc"):
    if isNum(i):
        counter += 1
print(counter)
