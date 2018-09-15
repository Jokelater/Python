#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import getpass
username = input("name:")
password = getpass.getpass("password:")

if username == 'jack' and password == '123':
    print("login")
else:
    print("try,again!")