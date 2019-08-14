#!/usr/bin/python
# -*- coding: utf-8-*-



#100-999水仙花级数
for num in range(100,1000):
    if (num%10)**3+(num // 10 % 10)**3+(num // 100)**3==num:
        print (num)


"""
完美数字
1+2+3+4
"""



#for num in range(1,1000):
