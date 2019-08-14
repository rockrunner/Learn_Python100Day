#!/usr/bin/python
# -*- coding: utf-8-*-

#输入月收入和五险一金
# 计算个人所得税



income=float(input('请输入月收入：'))
insurance=float(input('请输入五险一金:'))

base=income-insurance-5000

if base<=0:
    rate=0
    deduction=0
elif base<1000:
    rate=0.03
    deduction=500
elif base<3000:
    rate=0.08
    deduction=1005
elif base<5000:
    rate=0.1
    deduction=1750
elif base<7500:
    rate=0.25
    deduction=2050
elif base<10000:
    rate= 0.3
    deduction=2950
elif base<20000:
    rate=0.35
    deduction=3500
else:
    rate=0.45
    deduction=3750

tax=abs(base*rate-deduction)
#tax=base*rate-deduction

print ('应交纳的税是：￥%.2f元'%tax)
print ('到手的收入是：￥%.2f元'%(base+5000-tax))