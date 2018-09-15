#!/usr/bin/env python
# _*_ coding:utf-8 _*_

user = 'admin'
password = '123'
a = input("please input your username:")
b = input("please input your password:")
counter = 1

while a != user or b != password:
    print("错误：%d次,还可以输入：%d次" %(counter,5-counter))
    print("username or password error,""please try again!")
    counter = counter + 1
    a = input("please input your username:")
    b = input("please input your password:")

    if counter == 5:
        print("5次输入错误！已退出！")
        break

else:
    print("登录成功！")
