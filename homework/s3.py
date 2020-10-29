# -*- config:utf-8 -*-
"""
作者:计AI181宋曜通 201806030121
日期：2020年10月24日
"""
import random

def robot(num):
   if num & (num+ 1) == 0:
         if(num==1):
          num=num-1
          print("电脑拿走1个,剩余%d个"%num)
          return num
         else:
          xnum=num
          num = num - random.randint(1, int(num / 2))
          xnum=xnum - num
          print("电脑拿走%d个,剩余%d个"%(xnum,num))
          return num
   else:
    xnum=num
    while num & (num+1) !=0:
      num=num-1
    xnum=xnum - num
    print("电脑拿走%d个,剩余%d个" %(xnum,num))
    return num

def player(num):
    print("请输入拿走数量")
    x= int(input())
    z= int(num / 2)+1
    while x >=z:
       print("请输入一个小于%d的数"% z)
       x = int(input())
    num=num-x
    print("玩家拿走%d个,剩余%d个" % (x,num))
    return num


if __name__ == '__main__':
    print("是否开始游戏：")
    print("开始游戏：1")
    print("退出游戏：2")
    star = int(input())
    while star==1 :
     print("请输入总物品数")
     num= int(input())
     while  num<=2:
         print("请输入一个大于2的数字")
         num= int(input())
     print("游戏开始")
     while num>=0 :
        print("%d"%num)
        num=robot(num)
        if num==0 :
         print("玩家获胜")
         break
        if num ==1:
          print("电脑获胜")
          break
        num=player(num)
        if(num==0):
         print("电脑获胜")
         break
     print("是否继续游戏？")
     print("开始游戏：1")
     print("退出游戏：2")
     star = int(input())

