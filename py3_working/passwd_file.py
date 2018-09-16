#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#生成默认密码，如果输入则默认生成5位密码
#sys模块的avgs函数 用户接收用户输入的参数

import string
import random
import sys
def pw(num=5):
    pwd = ''
    all_choice = string.ascii_letters + string.digits

    for i in range(num):
        pwd += random.choice(all_choice)
    print(pwd)

if __name__ =='__main__':
    pw(int(sys.argv[1]))
