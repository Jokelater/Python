#!/usr/bin/env python
# _*_ coding:utf-8 _*_

num1 = 9
num2 = 6
while True:
    print('*'*20)
    print("num1:9\t\tnum2:6")
    print("请输入你想要进行的操作：\n加:+ 减:- 乘:* 除:/")
    print('*'*20)
    a = input(":")
    if a == '+':
        print("%d + %d = %d" %(num1,num2,num1+num2))
        break
    elif a == '-':
        print("%d - %d = %d" %(num1,num2,num1-num2))
        break
    elif a == '*':
        print("%d * %d = %d" %(num1,num2,num1*num2))
        break
    elif a == '/':
        print("%.02f / %.02f = %.02f" %(num1,num2,num1/num2))
        break
    else:
        print("输入有误，请重新输入: + - * /")