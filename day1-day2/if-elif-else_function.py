x=int(input('请输入x:'))


if x>1:
    y=3 * x-5
elif -1<=x<=1:
    y=x+2
else:
    y=5*x+3
print('f(%.0f)=%.0f'%(x,y))
