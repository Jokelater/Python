#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#小菜单
print("《今日菜单》")
menu = '''1.蒸羊羔儿
2.蒸熊掌
3.蒸鹿尾儿
4.烧花鸭
5.烧雏鸡
6.烧子鹅
选菜：'''
a = int(input(menu))
l1 = menu.split()
if a == 1:
    print(l1[a-1])
elif a == 2:
    print(l1[a-1])
elif a == 3:
    print(l1[a-1])
elif a == 4:
    print(l1[a - 1])
elif a == 5:
    print(l1[a-1])
elif a == 6:
    print(l1[a - 1])
else:
    print("别闹！")