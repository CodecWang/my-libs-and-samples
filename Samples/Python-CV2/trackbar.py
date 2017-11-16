# 滑动条示例
# ex2tron 2017年11月14日
# http://ex2tron.top
# 官方文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_trackbar/py_trackbar.html

import cv2
import numpy as np


def do_nothing(x):
    pass


img = np.zeros([300, 512, 3], np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('R', 'image', 0, 255, do_nothing)
cv2.createTrackbar('G', 'image', 0, 255, do_nothing)
cv2.createTrackbar('B', 'image', 0, 255, do_nothing)

switch = '0: OFF \n 1: ON'
cv2.createTrackbar(switch, 'image', 0, 1, do_nothing)

while(True):

    cv2.imshow('image', img)
    k = cv2.waitKey(1)
    if (k == ord('q')):
        break

    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if(s == 1):
        img[:] = [b, g, r]
    else:
        img[:] = 0

cv2.destroyAllWindows()
