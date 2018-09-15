#!/usr/bin/env python
# _*_ coding:utf-8 _*_

try:
    a = int(input("please input a num:"))
    print(a)
except ValueError as e:
    print(e,"输入的类型有错误！请输入一个数值型")

