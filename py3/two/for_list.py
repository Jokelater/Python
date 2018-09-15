#!/usr/bin/env python
# _*_ coding:utf-8 _*_

l1 = []
l1.append(int(input("num1:")))
l1.append(int(input("num2:")))
for i in range(8):
    l1.append(l1[i]+l1[i+1])
print(l1)

# l1.append = int(input("num1:"))
# l1.append = int(input("num2:"))
# num = input("num")
#
# for i in range(8):
#     print(l1)