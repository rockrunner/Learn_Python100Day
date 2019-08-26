#!/usr/bin/python
# -*- coding: utf-8-*-




def main():
    str1='hello world'
    # print (len(str1))
    # print (str1.capitalize())
    # print (str1.upper())
    # print (str1.find('o'))
    # print (str1.startswith('L'))
    # print (str1)
    list1=[1,2,3,4,5,6,7,8,9]
    print (list1)
    list2=['hellao']*5
    print (list2)
    print (len(list1))
    print (list1[0])
    print (list1[4])
    print (list1[-3])
    list1[2]=12
    print (list1)
    list1.append(39)
    print (list1)
    list1.insert(1,400)
    print (list1)
    list1+=[1000,2000]
    print (list1)
    print (len(list1))
    list1.remove(39)
    print (list1)
    if 9 in list1:
        list1.remove(9)
        print (list1)
    del list1[0]
    print (list1)
    list1.clear()

    print(list1)


def liebiao():
    furits=['apple','grape','strawbeety','waxxberry','banana']
    furits+=['pipaya','pear','mango']
    for furit in furits:
        print (furit.title()),
    print ('\n')

    furits2=furits[1:4]
    # print furits2

    furits3=furits
    # print furits3
    furits4=furits[:]
    # print furits4
    furits5=furits[-3:-1]
    print (furits5)
    furits6=furits[::-1]
    print (furits6)







if __name__=='__main__':
     # main()
     liebiao()
