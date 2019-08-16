#!/usr/bin/python
# -*- coding: utf-8-*-

# def add(*args):
#     total=0
#     for val in args:
#         total+=val
#     return total
#
#
#
#
# print (add(1,2,3,5))
#

# def fool():
#     b='hello'
#     # print (b)
#     def bar():
#         c=True
#         print (a)
#         print (b)
#         print (c)
#         print ("good")
#     bar()
#
# if __name__=="__main__":
#     a=100
#     fool()
    #print (b)#NameError: name 'b' is not defined
#yoga 每天做ｙｏｇａ是每个人的必修课，就像每天要吃饭，要睡觉，每天要做ｙｏｇａ，但是ｙｏｇａ的针对性是很强的，我要做的不是市场上的练习身体动作，因为我没有时间
def foo():
    global a
    a=200
    print (a)
if __name__=='__main__':
    a=100
    foo()

    print(a)