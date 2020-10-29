# -*- config:utf-8 -*-
"""
作者:计AI181宋曜通 201806030121
日期：2020年10月24日
"""
import random
door=[1,2,3]
redoor=[1,2,3]
xdoor=[1,2,3]
gift=random.randint(1,3)
#print("礼物在%d号门"%gift)
print("请从1,2,3号门中选择一个门")
choose=int(input())
assert choose>0 and choose<4
print("选择了%d号门"%door[choose-1])
if choose!=gift :
   redoor.remove(gift)
redoor.remove(choose)
#print(redoor)
x=random.choice(redoor)
print("管理员打开了%d号门"%x)
xdoor.remove(x)
xdoor.remove(choose)
print("是否改选%d号门"%xdoor[0])
print("改选:1")
print("坚持不改:2")
y=int(input())
assert y==1 or y==2
if y==1:
    choose=xdoor[0]

if choose==gift:
    print("恭喜获得车")
else:  print("获得山羊")
