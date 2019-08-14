a=5
b=2
c=3
d=5
e=6
a+=b
a-=c
a*=d
a/=e
print("a =",a)
flag1=3>2
flag2=2<1
flag3=flag1 and flag2
flag4=flag1 or flag2
flag5=not flag1
print("flag1=",flag1)
print("flag2=",flag2)
print("flag3=",flag3)
print("flag4=",flag4)
print("flag5=",flag5)

#practise1
"""
将华氏温度转化为摄氏温度
F=1.8c+32
"""
f=float(input('请输入华氏温度：'))
c=(f-32)/1.8

#print('%f华氏=%f摄氏度'%(f,c))
#practise2
"""
输入半径计算圆的周长和面积
author:骆昊
learner:Tao Li
"""
import math
radius=float(input('请输入圆的半径'))
L=2*math.pi*radius
S=math.pi*radius*radius
#print('圆的周长:%.2f，圆的面积:%.2f'%(L,S))

#practise3
"""
输入年份，判断是否是闰年
闰年Ture 否输出Flase

"""
year=int(input('请输入年份：'))
if year%4==0:
    print("%.0f是闰年"%year)
else:
    print("%.0f不是闰年"%year)

#分支结构的应用场景
"""""
地图导航，从浦东到浦西，有两条可选路径，到浦东南路与潍坊路叉路口，向左转走南浦大桥，向右转走复兴东路隧道
看完电影，选择回丈母娘家或者选择回自己家
去吃饭，选择吃拉面或者选择吃牛肉汤，吃完饭选择休息或者选择睡觉
去上班，选择开车或者坐地铁，开车到公司选择停在公司地下车库或者选择停在露天停车场
"""
