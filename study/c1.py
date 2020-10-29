# -*- config:utf-8 -*-
"""
作者:计AI181宋曜通 201806030121
日期：2020年10月13日
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img=cv2.imread("D:\pycharm\PycharmProject\img\difa.jpg")
# text = '''On a dark  desert highway, cool wind in my hair Warm smell of colitas, rising up through the air Up ahead in the distance, I saw a shimmering light My head grew heavy and my sight grew dim I had to stop for the night There she stood in the doorway; I heard the mission bell And I was thinking to myself, "This could be Heaven or this could be Hell" Then she lit up a candle and she showed me the wa\n'''
# print(text);
# for char in '-.,;\n"\'':
#     text = text.replace(char,' ')
#
# text.split(' ')[0:20]
#
# print(text)
import random

# i=int(input())
# z=int(i/2)
# while i<z :




# 100以内的2n次方-1的数
# count = 1
# while count <= 100:
#     if count & (count+ 1) == 0:
#        print(count)
#     count = count + 1

#颜色通道
# b=img.copy()
# b[:,:,1] = 0
# b[:,:,2] = 0
# g=img.copy()
# g[:,:,0] = 0
# g[:,:,2] = 0
# r=img.copy()
# r[:,:,0] = 0
# r[:,:,1] = 0
# top_size,bottom_size,left_size,right_size=(50,50,50,50)
# #复制最边缘的像素
# replicate=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size, borderType=cv2.BORDER_REPLICATE)
# #反射法 FEDCBA|ABCDEFGH|HGFEDCBA
# reflect=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size, cv2.BORDER_REFLECT)
# #反射法 以最边缘的像素为轴 GFEDCB|ABCDEFGH|GFEDCBA
# reflect101=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size, cv2.BORDER_REFLECT_101)
# #外包装法 cdefgh|abcdefgh|abcdefg
# warp=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size, cv2.BORDER_WRAP)
# #常亮法 常数值填充
# constant=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size, cv2.BORDER_CONSTANT, value=0)
#
# plt.subplot(231),plt.imshow(replicate,'gray'),plt.title('replicate')
# plt.subplot(232),plt.imshow(reflect,'gray'),plt.title('reflect')
# plt.subplot(233),plt.imshow(reflect101,'gray'),plt.title('reflect101')
# plt.subplot(234),plt.imshow(warp,'gray'),plt.title('warp')
# plt.subplot(235),plt.imshow(constant,'gray'),plt.title('constant')
# plt.show()
#
# imgt=cv2.imread("D:\pycharm\PycharmProject\img\iop.jpg")
# print(img.shape)
# print(imgt.shape)
# imgt=cv2.resize(imgt,(0,0),fx=0.5,fy=0.5)
# # imgt=cv2.resize(imgt,(281,500))
# print(img.shape)
# print(imgt.shape)
# imgt=cv2.resize(imgt,(500,281))
# print(img.shape)
# print(imgt.shape)
# #img=cv2.resize(img,(0,0),fx=1.5,fy=2) x方向扩大1.5倍，y方向扩大2倍
# res=cv2.addWeighted(img,0.6,imgt,0.4,3)
# cv_show("add",res)

#超过阈值的部分取最大 否则取0
ret,the1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#与THRESH_BINARY相反
ret,the2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
#大于阈值部分的设为阈值，否则不变
ret,the3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#大于阈值部分不变，否则设为0
ret,the4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
#THRESH_TOZERO的相反
ret,the5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)





