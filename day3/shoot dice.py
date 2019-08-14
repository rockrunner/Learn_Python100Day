#!/usr/bin/python
# -*- coding: utf-8-*-
"""
掷筛子决定做什么事情
"""

from random import randint

decision=randint(1,6)
print (decision)

if decision==1:
    print ('打脸')
elif decision==2:
    print ('洗衣服')
elif decision==3:
    print ('打架')
elif decision==4:
    print ('喝水')
elif decision==5:
    print ('吃肉')
else:
    print ('倒垃圾')