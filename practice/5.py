#!/usr/bin/python
#-*- coding: utf-8 -*-
#Author:      hz
#Environment: Linux & Ubuntu 17.10
#Filetype:    Python Source Code
#Tool:        Vim
#Date:        2018-02-09
#Decription:  输入三个整数x，y，z，请把这三个数由小到大输出

seq = []

for i in range(3):
    num = int(raw_input("请输入整数："))
    seq.append(num)
seq.sort()
print seq


