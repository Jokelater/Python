#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def defaulter(x,y=2):
    print("#" * (x*y))

defaulter(10)

def fibs(num):
    fib = [0,1]
    for i in range(num - 2):
        fib.append(fib[-1] + fib[-2])
    return fib

print(fibs(10))
print(fibs(20))