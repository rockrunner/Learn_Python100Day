
"""
质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数
"""
import math
a=int(input('请输入一个数字：'))
# c=a//2
# print(c)
# b=int(math.sqrt(a))
# b=int(a)
# print(b)
if a>1:
    for i in range(2,a):
      if  a%i==0:
          print('不是素数')
          break
    else:
         print('%d这个数是素数'%a)

else:
    print('输入不合法')