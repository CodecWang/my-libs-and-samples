# 几何变换
# ex2tron 22017年11月14日
# http://ex2tron.top
# 官方python-opencv文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html#geometric-transformations


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('material/lena.jpg', 0)
cv2.imshow('original', img)

# 缩放
res = cv2.resize(img, (28, 28))
cv2.imshow('resized', res)
# 比例缩放
res2 = cv2.resize(img, None, fx=0.5, fy=0.5)
cv2.imshow('resized', res2)

# 平移
rows, cols = img.shape
# 平移矩阵(参考官方文档)
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('translation', dst)

# 旋转
# 指定中心点、旋转角度（逆时针），缩放比例
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('rotation', dst)

# 仿射变换、透射变换（不常用，参考官方文档）

cv2.waitKey(0)
