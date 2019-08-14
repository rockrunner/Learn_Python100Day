#!/usr/bin/python
# -*- coding: utf-8-*-

from random import randint


i=randint(1,100)
k=0
while 1:
    num=int(input('请输入:'))
    if num>i:
        k+=1
        print('大了')
    elif num<i:
        k+=1
        print('小了')
    else:
        print ('猜对了')
        break
    print('你总共猜了%d次'%k)
if k>7:
    print ('智商不足,请充值')
else:
    print ('厉害了我的哥')