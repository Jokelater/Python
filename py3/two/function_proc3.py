#!/usr/bin/env python
# _*_ coding:utf-8 _*_

x = 100
def fun():
    x = 200
    y = 300
    print(locals())
fun()

