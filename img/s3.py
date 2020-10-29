# -*- config:utf-8 -*-
"""
作者:计AI181宋曜通 201806030121
日期：2020年10月28日
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


plt.figure(figsize=(15,6))
plt.suptitle("experiment three",fontsize=14,fontweight="bold")

img = cv2.imread("D:\pycharm\PycharmProject\img\syt.jpg",cv2.COLOR_BGR2BGRA)

img_BGR=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
show_img(img_BGR,"",1)

# 高斯滤波
img_Guassian = cv2.GaussianBlur(img, (5, 5), 0)

the4 =cv2.adaptiveThreshold(img_Guassian , 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
the4_BGR=cv2.cvtColor(the4,cv2.COLOR_GRAY2BGR)
show_img(the4_BGR,"GAUSSIAN+MEAN",2)
#卷积和
kernel = np.ones((3, 3), np.uint8)
#腐蚀
erosion = cv2.erode(the4, kernel, iterations=2)
erosion_BGR=cv2.cvtColor(erosion ,cv2.COLOR_GRAY2BGR)
show_img(erosion_BGR,"erode",3)
#膨胀
dilation = cv2.dilate(the4, kernel, iterations=1)
dilation_BGR=cv2.cvtColor(dilation ,cv2.COLOR_GRAY2BGR)
show_img(dilation_BGR,"dilate",4)
# 开运算
opening = cv2.morphologyEx(the4, cv2.MORPH_OPEN, kernel)
opening_BGR=cv2.cvtColor(opening ,cv2.COLOR_GRAY2BGR)
show_img(opening_BGR,"opening ",5)
#闭运算
closing = cv2.morphologyEx(the4, cv2.MORPH_CLOSE, kernel)
closing_BGR=cv2.cvtColor(closing ,cv2.COLOR_GRAY2BGR)
show_img(closing_BGR,"closing",6)
plt.show()