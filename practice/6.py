#!/usr/bin/python
#-*- coding: utf-8 -*-
#Author:      hz
#Environment: Linux & Ubuntu 17.10
#Filetype:    Python Source Code
#Tool:        Vim
#Date:        2018-02-09 
#Decription:  斐波那契数列

#1递推
def fib1(len):
    if len == 1:
        return [0]
    if len == 2:
        return [0, 1]
    seq = [0, 1]
    for i in range(len - 2):
        seq.append(seq[-2] + seq[-1])
    return seq

#2递归
def fib2(len):
    if len == 0:
        return 0
    if len == 1:
        return 1
    return fib2(len - 2) + fib2(len - 1)
#3生成器
def fib3(len):
    a = 0
    b = 1
    n = 0
    while n < len:
        yield a
        a, b, n = b, a + b, n + 1


print fib1(10)
q = []
for i in range(10):
    q.append(fib2(i))
print q
s = []
for i in fib3(10):
    s.append(i)
print s

