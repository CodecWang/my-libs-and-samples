# 霍夫圆变换
# ex2tron 22017年11月22日
# http://ex2tron.top
# 官方python-opencv文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html

import cv2
import numpy as np

img = cv2.imread('material/opencv_logo.png', 0)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # 画外圆
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # 画圆心
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('detected circles', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
