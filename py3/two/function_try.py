#!/usr/bin/env python
# _*_ coding:utf-8 _*_


s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']

for i in L:
    if i not in s:
        s.add(i)
print(s)