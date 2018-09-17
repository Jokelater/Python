#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 实现文件的备份功能
def cp_file():
    #源文件
    s_file = input("要备份的文件名：")
    #目标文件
    d_file = input("备份为文件名:")
    #这里需要注意如果复制的是二进制文件需要给‘rb’权限
    s_file_o = open(s_file,'r')
    #同理二进制文件给 ‘wb’权限
    d_file_o = open(d_file,'w')
    while True:
        #用data变量来存储源文件中取出来的每一行数据
        data = s_file_o.readline()
        #判断data是否为空，跳出循环
        if not data:
            break
        #将中的数据存放到目标文件中
        d_file_o.write(data)
    s_file_o.close()
    d_file_o.close()
cp_file()