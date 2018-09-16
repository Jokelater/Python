#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#统计指定文件，行数、单词数、字符数
__author__='JokeLate'

def wordCount(s):
    chars = len(s)
    words = len(s.split())
    lines = s.count('\n')
    print(lines,words,chars)
s=open("/etc/hosts").read()
wordCount(s)

#在由于我们是在远程所有没有结果，
#这条命令是在本地运行脚本的时候才会生效
if __name__ == '__man__':
    wordCount(s)