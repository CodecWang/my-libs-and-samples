# 图片平滑处理
# ex2tron 2017年11月14日
# http://ex2tron.top
# 官方文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html#filtering

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('material/lena.jpg', 0)
# 均值滤波
blur = cv2.blur(img, (5, 5))
# 高斯滤波
blur_gauss = cv2.GaussianBlur(img, (5, 5), 0)
# 中值滤波
blur_median = cv2.medianBlur(img, 5)

# 双边滤波（不常用，参考官方文档）

plt.subplot(221), plt.imshow(img, 'gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(blur, 'gray'), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(blur_gauss, 'gray'), plt.title('Guassian')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(blur_median, 'gray'), plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.show()
