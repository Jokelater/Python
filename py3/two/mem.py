#!/usr/bin/env python
# _*_ coding:utf-8 _*_

f = open('/proc/meminfo','r')
for lines in f:
    if lines.startswith("MemTotal:"):
        memTotal = int(lines.split()[-2]) /1024
    if lines.startswith("MemFree"):
        memFree = int(lines.split()[-2]) /1024
        break
print("MemTotal:%.2fMB + MemFree:%.2fMB = Use:%.2fMB" %(memTotal,memFree,memTotal - memFree))