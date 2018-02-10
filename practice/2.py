#!/usr/bin/python
#-*- coding: utf-8 -*-
#Author:      hz
#Environment: Linux & Ubuntu 17.10
#Filetype:    Python Source Code
#Tool:        Vim
#Date:        
#Decription: 企业发放的奖金根据利润提成，利润(I)低于或等于
#            十万元时，奖金可提10%; 利润高于10万元，低于20
#            万元时，低于10万元的部分按10%提成，高于10万元
#            的部分，可提成7.5%; 20万到40万之间时，高于20万
#            的部分，可提成5%; 40万到60万之间高于40万部分，
#            可提成3%；60万到100万之间时，高于60万元的部分
#            可提成1.5%,高于100万元时，超过100万元的部分按
#            1%提成，从键盘输入当月利润I，求应发奖金总数？
i = int(raw_input("请输入净利润："))

grade = [1000000, 600000, 400000, 200000, 100000, 0]

percent = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

money = 0

for j in range(0, 6):
    if i > grade[j]:
        money += (i - grade[j]) * percent[j]
        i = grade[j]
print "应发奖金：", money

