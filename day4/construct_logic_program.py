#!/usr/bin/python
# -*- coding: utf-8-*-



#100-999水仙花级数
# for num in range(100,1000):
#     if (num%10)**3+(num // 10 % 10)**3+(num // 100)**3==num:
#         print (num)
#

"""
完美数字
1+2+3=6 
6=3*2=1*6

1+2+14+4+7=28
496=1+2+248+4+128+8+62=496
"""



#for num in range(1,1000):
import math

# for num in range(1, 10000):
#     result = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             result += factor
#             if factor > 1 and num // factor != factor:
#                 result += num // factor
#     if result == num:
#         print(num)
#
# num=input('num:')
# print int((math.sqrt(num)))
#
#
for num in range(1,10000):#引入范围
   result=0#求和的小卡车
   for fac in range(1,int(math.sqrt(num))+1):#引入因子和因子范围，目的是找到因子
            if num%fac==0:#确认眼神，你是不是我的因子
                result+=fac#是就上车，装进小卡车
                if fac>1 and num//fac!=fac:#关键点：fac>1时 因子总是成对出现的，找到了一个就找到了另一个（除）,！=fac是因为16=4*4不是完美数
                    result+=num//fac
   if result==num:
       print(num)