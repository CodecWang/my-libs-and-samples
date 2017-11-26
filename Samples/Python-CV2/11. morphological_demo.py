# 形态学分析
# ex2tron 2017年11月15日
# http://ex2tron.top
# 官方文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

import cv2
import numpy as np

# 灰度图加载
img = cv2.imread('material/j.jpg', 0)
kernel = np.ones([5, 5], np.uint8)

# 1.腐蚀：物体为白色（常见应用：去除噪点）
erosion = cv2.erode(img, kernel, iterations=1)

# 2.膨胀（常见应用：去除噪点后，目标物体也缩小了，所以需要放大）
dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('original', img)
cv2.imshow('erosion', erosion)
cv2.imshow('dilation', dilation)
cv2.waitKey(0)

# 3.开操作：先腐蚀，后膨胀
img = cv2.imread('material/j_noise1.jpg', 0)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('original2', img)
cv2.imshow('opening', opening)
cv2.waitKey(0)

# 4.闭操作：先膨胀，后腐蚀（举例：去除洞）
img = cv2.imread('material/j_noise2.jpg', 0)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('original3', img)
cv2.imshow('closing', closing)
cv2.waitKey(0)

# 5.形态学梯度、6.顶帽、7.黑帽（不常用，参考官方文档）
