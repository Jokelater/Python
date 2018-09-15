#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys

for i in range (10):
    if i == 5:
        continue
    if i == 6:
        continue
    if i == 7:
        pass
    if i == 8:
        sys.exit()
    print(i)
else:
    print("end")