#!/usr/bin/python
# -*- coding: utf-8-*-

grade=int(input('请输入百分制成绩：'))
if grade>=90:
    rank='A'
elif grade<90 and grade>=80:
    rank='B+'
elif grade<=80 and grade>=70:
    rank='B-'
elif grade<=70 and grade>=60:
    rank='C'
else:
    rank='E'
print('对应的等级:',rank)