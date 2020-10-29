# -*- config:utf-8 -*-
"""
作者:计AI181宋曜通 201806030121
日期：2020年10月25日
"""
import  cv2

vc=cv2.VideoCapture("D:\pycharm\PycharmProject\img\suolong.mp4")
if vc.isOpened():
    open,frame=vc.read()
else:
    open=False
while open :
    ret,frame=vc.read()
    if frame is None:
        break
    if ret == True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('result',gray)
        if cv2.waitKey(30) & 0xFF==27:
            break
vc.release()
cv2.destroyAllWindows()