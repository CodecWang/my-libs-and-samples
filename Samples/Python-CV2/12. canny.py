# 滑动条示例
# ex2tron 2017年11月14日
# http://ex2tron.top
# 官方文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_trackbar/py_trackbar.html

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('material/lena.jpg', 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
