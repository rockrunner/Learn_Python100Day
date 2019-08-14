#!/usr/bin/python
# -*- coding: utf-8-*-

import math

a=int(input('a边长：'))
b=int(input('b边长:'))
c=int(input('c边长：'))
if a+b>c and b+c>a and c+a>b:
    L=a+b+c
    p=L/2
    S=math.sqrt((p-a)*(p-b)*(p-c))
    print ('周长：%.0f'%L)
    print ('面积：%f'%S)
else:
    print('不能构成三角')