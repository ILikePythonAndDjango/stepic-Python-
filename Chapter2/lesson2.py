# -*- coding: utf-8 -*-
# lesson 2.1: work with code: modules and import

'''
import lesson1
import fib

print(lesson1.greet("Hello"))
'''

"""
В первой строке ввода вводиться data - год, месяц, день
Во второй строке число дней n
Нужно вычеслить дату, которaя наступит через n дней с data.
"""

'''
import datetime
year, month, day = input().split()
n = int(input())
now_date = datetime.date(int(year), int(month), int(day)) + datetime.timedelta(n)
print(now_date.year, now_date.month, now_date.day)
'''
'''
from lesson1 import *

print(BadName)
print(greet("Student"))
'''
