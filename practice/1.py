#!/usr/bin/python
#-*- coding: utf-8 -*-
#Author:      hz
#Environment: Linux & Ubuntu 17.10
#Filetype:    Python Source Code
#Tool:        Vim
#Date:        
#Decription: 有1、2、3、4个数字，能组成多少个互不相同且
#无重复数字的三位数？都是多少？

nums = set()

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                nums.add(i * 100 + j * 10 + k)
print sorted(nums)
print "总共：%s" % len(nums)




