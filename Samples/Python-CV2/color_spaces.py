# 颜色空间
# ex2tron 22017年11月14日
# http://ex2tron.top
# 官方python-opencv文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces


import cv2
import numpy as np

# opencv中hsv各值是有范围的：
# Hue：[0,179]，Saturation：[0,255]，Value： [0,255]

# 想知道绿色的hsv值：
green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)
# 此时，可以用范围：[H-10, 100,100] ~ [H+10, 255, 255]表示绿色
