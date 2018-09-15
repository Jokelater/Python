import random
print("*"*20)
all_choose = ['石头','剪刀','布']
win_list = ['石头','剪刀'],['布','石头'],['剪刀','石头']
#定义用户选择列表li
li = """(0)石头
(1)剪刀
(2)布"""
manWin = 0
pcWin = 0
while manWin<2 and pcWin<2:
    co = int(input(li + "\nplease input your choose[(0)/(1)/(2)]:"))
    manChoose = all_choose[co]
    computer = random.choice(all_choose)
    print("your choose:%s computer choose:%s"%(manChoose,computer))
    if manChoose == computer:
        pass
    elif [manChoose,computer] in win_list:
        manWin+=1
        #print("你赢了！")
    else:
        #print("你输了！")
        pcWin+=1

if manWin == 2:
    print("your Win!")
elif pcWin == 2:
    print("your Lose")

