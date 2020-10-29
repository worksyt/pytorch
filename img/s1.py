#-*- config:utf-8 -*-
"""
作者:计AI181宋曜通 201806030121
日期：2020年10月20日
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

def img_show(img):
    cv2.namedWindow("Image")
    cv2.imshow("Image", img)

def img_load(img):
    cv2.imwrite("D:\pycharm\PycharmProject\img\save.jpg", img)

def img_flip(img):
    sp = cv2.flip(img, 0)
    cz = cv2.flip(img, 1)
    sc = cv2.flip(img, -1)

    cv2.imshow("Horizontally", sp)
    cv2.imshow("Vertically", cz)
    cv2.imshow("Horizontally & Vertically",sc)

def img_move(img):
    # 图像平移 下、上、右、左平移
    M = np.float32([[1, 0, 0], [0, 1, 100]])
    img_down = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

    M = np.float32([[1, 0, 0], [0, 1, -100]])
    img_up = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

    M = np.float32([[1, 0, 100], [0, 1, 0]])
    img_right = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

    M = np.float32([[1, 0, -100], [0, 1, 0]])
    img_left = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

    # 显示图形
    cv2.imshow("down", img_down)
    cv2.imshow("up", img_up)
    cv2.imshow("right", img_right)
    cv2.imshow("left", img_left)

def img_rotation(image):
    # 原图的高、宽 以及通道数
    rows, cols, channel = image.shape

    M = cv2.getRotationMatrix2D((cols / 2, rows / 2),30, 1)

    rotated = cv2.warpAffine(image, M, (cols, rows))

    # 显示图像
    cv2.imshow("rotated", rotated)


def gasuss_noise(image, mean=0, var=0.001):

  image = np.array(image/255, dtype=float)
  noise = np.random.normal(mean, var ** 0.5, image.shape)
  out = image + noise
  if out.min() < 0:
    low_clip = -1.
  else:
    low_clip = 0.
  out = np.clip(out, low_clip, 1.0)
  out = np.uint8(out*255)
  cv2.imshow("gasuss", out)


def mytry( ):
     ''
img = cv2.imread("D:\pycharm\PycharmProject\img\difa.jpg")

shape_op = np.array([[0, -1, 0],
                   [1, 3, -1],
                   [0, -1, 1]], np.float32)

ans = cv2.filter2D(img, -1, shape_op)

cv2.imshow("mytry", ans)


def  fly( ):
    img = cv2.imread("D:\pycharm\PycharmProject\img\difa.jpg",0)
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dftShift = np.fft.fftshift(dft)
    result = 20 * np.log(cv2.magnitude(dftShift[:, :, 0], dftShift[:, :, 1]))

    plt.subplot(121)
    plt.imshow(img, cmap='gray')
    plt.title('begin')
    plt.axis('off')
    plt.subplot(122)
    plt.imshow(result, cmap='gray')
    plt.title('end')
    plt.axis('off')
    plt.show()

def refly():

    img = cv2.imread("D:\pycharm\PycharmProject\img\difa.jpg", 0)
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dftShift = np.fft.fftshift(dft)
    ishift = np.fft.ifftshift(dftShift)
    iimg = cv2.idft(ishift)
    iimg = cv2.magnitude(iimg[:, :, 0], iimg[:, :, 1])
    plt.subplot(121)
    plt.imshow(img, cmap='gray')
    plt.title('begin')
    plt.axis('off')
    plt.subplot(122)
    plt.imshow(iimg, cmap='gray')
    plt.title('end')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':

    img = cv2.imread("D:\pycharm\PycharmProject\img\difa.jpg")
    #img_show(img)
    #img_load(img)
    #img_flip(img)
    #img_move(img)
    #img_rotation(img)
    #gasuss_noise(img)
    #img= cv2.blur(img, (5, 5))
    #img= cv2.medianBlur(img, 5, 0)
    #img_Guassian = cv2.GaussianBlur(img, (5, 5), 0)
    #img_show(img)
    mytry()
    #fly()
    #refly()

    cv2.waitKey(0)
    cv2.destroyAllWindows()