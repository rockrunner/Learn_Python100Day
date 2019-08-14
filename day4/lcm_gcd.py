#!/usr/bin/python
# -*- coding: utf-8-*-



a=input("please type a number:")
b=input("please type a number:")
#
# if a>b>1 and a%b==0:
#     print ('gcd%d'%b)
# elif 1<a<b and b%a==0 :
#     print ('gcd%'%a)
# elif a==b and a!=0 and b!=0:
#     print ('gcd%d'%(a and b))
# elif  a%b!=0:
#     print ('gcd%d'%1)
# elif a<1 or b<1 :
#     print ('非法输入')

if a>b:
    a,b=b,a
#print (a,b)
for c in range(a,0,-1):
    if a%c==0 and b%c==0 :
     print ('gcd%d'%c)
     print ('lcm%d'%((a*b)/c))
     break
