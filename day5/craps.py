#!/usr/bin/python
# -*- coding: utf-8-*-
"""
两个筛子一起摇：
             如果第一次就摇出两色子点数之和是7，11，那么玩家就直接赢，游戏结束

             同样如果第一次摇出的是2，3，12，那么直接就是庄家赢，游戏结束

             如果以上点数都不是，比如如果摇到5，那么记录下5，玩家重新摇，如果再次摇到了5，那么玩家赢，游戏结束
                                                                如果摇到了7，那么对方的庄家赢，游戏结束
"""
#
from random import randint
#


money=1000
while money>0 :
     print ("你的总资产：%d"%money)
     deb=input('请下注：')
     while True:
         if 0<deb<=money:
             break
     needs_go_on = False
     first = randint(1, 6) + randint(1, 6)
     print (first)
     if first==7 or first==11 :
         print ('player win')
         money+=deb
     elif first==2 or first==3 or first==12:
         print ('banker win')
         money-=deb
     else:
         needs_go_on= True

     while needs_go_on:
         current=randint(1,6)+randint(1,6)
         print (current)
         if current==7:
             print ('banker win')
             money-=deb
             needs_go_on=False
         elif current==first:
             print ('player win')
             money+=deb
             needs_go_on=False
print ('game over')



# from random import randint
#
# money = 100000
# while money > 0:
#     print('你的总资产是:', money)
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注: '))
#         if 0 < debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print('玩家摇出了%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜!')
#         money -= debt
#     else:
#         needs_go_on = True
#
#     while needs_go_on:
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点' % current)
#         if current == 7:
#             print('庄家胜')
#             money -= debt
#             needs_go_on = False
#         elif current == first:
#             print('玩家胜')
#             money += debt
#             needs_go_on = False
#
# print('你破产了, 游戏结束!')

#比人因小时候养成了许多不自知的习惯，从而享受了现在不自知的习惯的影响，从未间断。恐惧不会因为你了解他的内容而消失
#正如就算你知道你小时候的习惯是怎么样形成的，也改变不了这段时光对你的影响，能改变这段历史的唯一关键就是让他从你的习惯里消失，不再缠绕你的现在。
#所以你必须警觉自己的习惯性爆发，注意他是怎样影响你的思考和你的情绪，以及你的生活的。这需要智慧才能破除，智慧就来自于。。。