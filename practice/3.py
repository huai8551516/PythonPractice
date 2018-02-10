#!/usr/bin/python
#-*- coding: utf-8 -*-
#Author:      hz
#Environment: Linux & Ubuntu 17.10
#Filetype:    Python Source Code
#Tool:        Vim
#Date:        
#Decription:  一个整数，它加上100和加上268后都是一个完全平方数，
#             请问该数是多少？

from math import sqrt

max = int(raw_input("你要求n以内的整数："))
num_seq = []
for i in range(max):
    num1 = int(sqrt(i + 100))
    num2 = int(sqrt(i + 268))
    if num1 ** 2 == i + 100 and \
       num2 ** 2 == i + 268:
        num_seq.append(i)
print num_seq
