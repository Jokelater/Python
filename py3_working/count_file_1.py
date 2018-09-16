#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#引用count_file ，自定义模块

import count_file

with open('/etc/passwd') as f:
    count_file.wordCount(f.read())
