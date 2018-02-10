#!/usr/bin/python
#-*- coding: utf-8 -*-
#Author:      hz
#Environment: Linux & Ubuntu 17.10
#Filetype:    Python Source Code
#Tool:        Vim
#Date:        2018-02-09 
#Decription:  输出九九乘法表


for i in range(1, 10):
    for j in range(1, i + 1):
        if 3 <= i <= 4 and j == 3:
            print '',
        print "%dx%d=%d" % (j, i, i * j),
    print ''



