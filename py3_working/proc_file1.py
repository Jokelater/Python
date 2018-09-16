#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#利用计算列表长度的方法来计算，进程文件的个数
import os
list = []
def isNum(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            break
    else:
        #将进程id，添加到list列表中
        list.append(s)

for li in os.listdir("/proc"):
    isNum(li)

#打印进程id
print(list)
#打印出列表的长度，就是进程id的数量
print(len(list))