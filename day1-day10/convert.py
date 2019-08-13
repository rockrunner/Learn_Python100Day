"""
厘米和英寸的转换
"""

value=float(input('请输入长度：'))
unit=input('请输入单位：')
if unit=='feet'or unit=='英寸':
    print('%2f英寸=%.0f厘米'%(value,value*2.54))
elif unit=='cm' or unit=='厘米':
    print('%.2f厘米=%.2f英寸'%(value,value/2.54))