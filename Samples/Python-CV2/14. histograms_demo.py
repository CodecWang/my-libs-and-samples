# 直方图示例
# ex2tron 22017年11月17日
# http://ex2tron.top
# 官方python-opencv文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html#histograms-getting-started


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('material/lena.jpg', 0)
# 1.计算直方图
# 第二个参数，灰度图为[0]，彩色图[0]/[1]/[2]代表b/g/r
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# 方式二：使用numpy计算直方图
# hist = np.bincount(img.ravel(), minlength=256)

# 2.绘制直方图
# img.ravel()相当于img.reshape(-1)变成1行n列
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

# 3.直方图均衡化（Histogram Equalization）
# 归一化公式 value = (value-min)*255/(max-min)
equ = cv2.equalizeHist(img)
# 两张照片并排
res = np.hstack((img, equ))
cv2.imshow('Equalization', res)
cv2.waitKey(0)

# 4.自适应局部均衡化（图像分成小块，每块进行均衡化）
img = cv2.imread('material/tsukuba_l.jpg', 0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
res = np.hstack((img, cl1))
cv2.imshow('adaptive equalization', res)
cv2.waitKey(0)

# 5.二维直方图/反向投影（参考官方文档）
