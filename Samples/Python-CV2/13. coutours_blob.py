# Blob分析
# ex2tron 2017年11月14日
# http://ex2tron.top
# 官方文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html

import cv2
import numpy as np
import matplotlib.pyplot as plt

img_origin = cv2.imread('material/num2.jpg')
img = cv2.cvtColor(img_origin, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold', thresh)

# 1.寻找轮廓：物体白，背景黑
image, contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

# 2.画出轮廓，-1代表画出所有轮廓，n代表第几条轮廓，从0开始
# img = cv2.drawContours(img_origin, contours, -1, (0, 255, 0), 3)
# 或者：画出第2条轮廓
cnt = contours[1]
img = cv2.drawContours(img_origin, [cnt], 0, (0, 255, 0), 3)
cv2.imshow('draw contours', img)

# 3.图像的矩
M = cv2.moments(cnt)
# print(M)
# 重心/质心/形心：
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
print(cx, cy)

# 4.面积
area = cv2.contourArea(cnt)
# 或者
# area = M['m00']
print(area)

# 5.周长
perimeter = cv2.arcLength(cnt, True)
print(perimeter)

# 6.（最小）外接矩
# 外接矩：不旋转，返回左上角点、宽高度
x, y, w, h = cv2.boundingRect(cnt)
cv2.rectangle(img_origin, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('rectangle', img)
# 最小外接矩：有旋转，返回box对象：box与rectangle的区别就在于box有旋转角
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
# np.int0:矩阵全部转换为int类型，np.int会出错
box = np.int0(box)
# 或者用下面的语句转换
# box = box.astype(np.int32)
img = cv2.drawContours(img_origin, [box], 0, (0, 0, 255), 2)
cv2.imshow('mini rectangle', img)

# 7.最小外接圆
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img = cv2.circle(img_origin, center, radius, (0, 255, 0), 2)
cv2.imshow('mini circle', img)

# 8.旋转矫正
angle = rect[2]
rectify_angle = 90 - abs(angle) if 45 < abs(angle) < 90 else angle
# 以图片中心旋转
rows, cols, channels = img_origin.shape
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), rectify_angle, 1)
# 或以最小外接矩中心旋转
# center = rect[0]
# M = cv2.getRotationMatrix2D((center[0] / 2, center[1] / 2), rectify_angle, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('rectify', dst)

# 8.凸包，轮廓拟合暂不介绍，参考官网

cv2.waitKey(0)
