# _*_ coding:utf-8 _*_
#功能：用于列出 当前文件的所有子目录和子文件

import os
import sys

def print_files(path):
    isdir,isfile,join = os.path.isdir,os.path.isfile,os.path.join
    lsdir = os.listdir(path)

    dirs = [i for i in lsdir if isdir(join(path,i))]
    files = [ i for i in lsdir if isfile(join(path,i))]

    if files:
        for f in files:
            print(join(path,f))
    if dirs:
        for d in dirs:
            print_files(join(path,d))
print_files('/home')

# print_files(sys.argv[1])
