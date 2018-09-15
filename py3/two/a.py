#!/usr/bin/env python
# _*_ coding:utf-8 _*_

n = ''
l1= ['1.python','2.java','3.php','4.js','5.运维']
pro = '''1.python
2.java
3.php
4.js
5.运维'''
while not n:
    print("科目列表")
    n = int(input(pro + "\t请选择："))
    if n <= len(l1):
        print("您选择了：" + l1[n-1])
    else:
        print("屌丝伟！")