#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#文件或目录创建脚本
import os
#用户选择新建目录还是文件
def panDuan():
    b = int(input('1.创建文件 2.创建文件夹 [1/or/2]'))
    #接收用户的输入如果文件运行函数creatFile,如果是文件夹运行函数creatDir
    if b == 1:
        creatFile()
    elif b == 2:
        creatDir()
    else:
        print("别闹！")

def creatDir():
    a = input("文件夹名称：")
    #判断文件名是否存在
    if os.path.exists(a):
        print("已存在！")
    #创建文件夹
    os.makedirs(a)

def creatFile():
    a = input("文件名称：")
    #拆分文件名防止用户在没有的文件夹中创建文件
    b = os.path.split(a)
    if os.path.exists(b[0]):
        os.mknod(b[1])
    else:
        os.makedirs(b[0])
        os.mknod(b[1])
panDuan()