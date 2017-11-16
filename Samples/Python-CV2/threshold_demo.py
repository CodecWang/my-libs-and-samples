# 阈值分割
# ex2tron 22017年11月14日
# http://ex2tron.top
# 官方python-opencv文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding


import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('material/lena.jpg', 0)
cv2.imshow('original', img)

# 最常用的阈值分割：
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary threshold', thresh1)

# 最容易忽略的，反相阈值：
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# 当然也可以用取反操作：
# thresh2 = 255 - thresh1
cv2.imshow('binary reverse threshold', thresh2)

# 自适应阈值对比手动阈值
img2 = cv2.imread('material/dave.jpg', 0)

ret, th1 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(
    img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(
    img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img2, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
