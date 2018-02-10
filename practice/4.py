#!/usr/bin/python
#-*- coding: utf-8 -*-
#Author:      hz
#Environment: Linux & Ubuntu 17.10
#Filetype:    Python Source Code
#Tool:        Vim
#Date:        2018-02-09
#Decription: 输入某年某月某日，判断这一天是这一年的第几天？

def leapYear(year):
    """
      判断是否闰年，是返回True，否返回False
      参数年份
    """
    if year % 400 == 0 or \
       year % 100 != 0 and \
       year % 4 == 0:
        return True
    else:
        return False
def theYearOfDay(year, month, day):
    months_day = [31, 28, 31, 30, 31, 30, 
                  31, 31, 30, 31, 30, 31
                 ]    
    sum_days = 0
    for i in range(month - 1):
        if leapYear(year) and month >= 3:
            sum_days += 1
        sum_days += months_day[i]
    sum_days += day
    return sum_days

if __name__ == "__main__":
    year = int(raw_input("请输入年："))
    month = int(raw_input("请输入月："))
    day = int(raw_input("请输入日："))
    print "%d年的第%d天" % (year, theYearOfDay(year, month, day))

