#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import random
all_pro = ['虫子','棒子','老虎','鸡']
win_pro = ['虫子','棒子'],['棒子','老虎'],['老虎','鸡'],['鸡','虫子']
pro = '''0.鸡
1.虫子
2.棒子
3.老虎
'''
rWin = 0
pWin = 0
while rWin<2 and pWin<2:
    co = int(input(pro+"选择一个："))
    Pc = random.choice(all_pro)
    Rc = all_pro[co]
    print("电脑选择了：%s 你选择了：%s" %(Pc,Rc))
    if Pc == Rc:
        print("打和局！")
    elif [Rc,Pc] in win_pro:
        rWin = rWin + 1
    else:
        pWin = pWin + 1
if rWin == 2:
    print("your Successfully!")
else:
    print("your loser!")
