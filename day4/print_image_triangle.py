#!/usr/bin/python
# -*- coding: utf-8-*-
"""
please print floowing image
单细胞生物请注意，这是双细胞生物的地界!!!
use double "for" and use same i to control ,outside "for" use i to control times(row).inside use "for" to control number of *
its incredible! its magic!
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""
# n=input('')
# while n<5:
#     for i in range (0,n+1):
#           n+=1
#     print ('*''\t'),


row=int(input('请输入您想制定的图形的行数please type the row-number of your image：'))
# for i in range(row):
#     for j in range(i+1):
#         print ('*'),
#     print ('\n')


# for i in range(row):
#     for j in range(row):
#         print ('*'),
#     print ('*')
# #print ('\n')
#
#
#
#
#
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(''),#输出空
#         else:
#             print('*'),
#     print('\n')

for i in range(row):
    for j in range(row):
        if j<row-1-i:
            print (''),
        else:
            for k in range( i-1 ):
                    print ('*'),
    print ('\n')

"""
3层for循环，可耻的匿了，实在不明白这是如何在内部运行的
"""