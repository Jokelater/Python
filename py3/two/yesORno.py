#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# y = input("please choose [YES|NO|Y|N]:")
# yn = y.lower()
# if yn == 'yes' or yn == 'y':
#     print("your choose yes")
# elif yn == 'no' or yn == 'n':
#     print("your choose no")
# else:
#     print("input error,please choose again!")
s = 0
x = 1
while x<=100:
    s = x + s
    x = x + 2
print(s)
