#!/usr/bin/python
# -*- coding: utf-8-*-


"""
分析：f(n-1)+f(n-2)=f(n)
1+1=2+3=5+6=11+12=23+24=47



"""
i=0
j=1

# for k in range(15):
#      i,j=j,i+j
#      print (i)


i=0
j=1
for k in range(10):
    i,j=j,i+j
    print (i,j)