# -*- config:utf-8 -*-
"""
作者:计AI181宋曜通 201806030121
日期：2020年10月25日
"""
import cv2
import hist as hist
import numpy as np
from matplotlib import pyplot as plt

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_img(img,title,pos):
    img_RGB=img[:,:,::-1]
    plt.subplot(2,3,pos)
    plt.title(title)
    plt.imshow(img)

def show_histo(hist,title,pos,color):
    plt.subplot(2,3,pos)
    plt.title(title)
    plt.xlabel("bins")
    plt.ylabel("pixels")
    plt.xlim([0,256])
    plt.plot(hist,color=color)


plt.figure(figsize=(15,6))
plt.suptitle("experiment two",fontsize=14,fontweight="bold")

img = cv2.imread("D:\pycharm\PycharmProject\img\syt.jpg",cv2.COLOR_BGR2BGRA)
#cv2.imshow("img",img)
#灰度直方图
hist_img=cv2.calcHist([img],[0],None,[256],[0,256])
img_BGR=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
show_img(img_BGR,"",1)
show_histo(hist_img,"gray img histogram",4,"m")
# 均值滤波
img_mean = cv2.blur(img, (5, 5))
# 中值滤波
img_median = cv2.medianBlur(img, 5, 0)
# 高斯滤波
img_Guassian = cv2.GaussianBlur(img, (5, 5), 0)

#全局阈值
ret,the1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
the1_BGR=cv2.cvtColor(the1,cv2.COLOR_GRAY2BGR)
show_img(the1_BGR,"Global Threshold",2)

#自适应阈值
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
the2_BGR=cv2.cvtColor(the1,cv2.COLOR_GRAY2BGR)
show_img(the2_BGR,"MEAN",3)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
the3_BGR=cv2.cvtColor(the1,cv2.COLOR_GRAY2BGR)
show_img(the3_BGR,"GAUSSIAN",5)
the4 =cv2.adaptiveThreshold(img_Guassian , 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
the4_BGR=cv2.cvtColor(the4,cv2.COLOR_GRAY2BGR)
show_img(the4_BGR,"GAUSSIAN+MEAN",6)
plt.show()


