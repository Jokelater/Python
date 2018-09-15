#!/usr/bin/env python
# _*_ coding:utf-8 _*_
print("*"*30)
score = int(input("please input your scour:"))
if score > 90:
    print("A")
elif score > 70:
    print("B")
elif score > 60:
    print("C")
elif score < 60:
    print("不及格")
    print("pass")
else:
    print("请输入正确的scour!")
print("*"*30)