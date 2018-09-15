
#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def useMem():
    f = open('/proc/meminfo','r')
    for i in f:
        i.startswith("MemTotal:")
        print(i.split()[-1])
        i.startswith("MemFree:")
        print(i.split()[-1])
        break
