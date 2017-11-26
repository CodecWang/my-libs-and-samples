# 常用的画图函数
# ex2tron 2017年11月14日
# http://ex2tron.top
# 官方文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html

import cv2
import numpy as np

# 画直线
img = np.zeros([512, 512, 3], np.uint8)
# 起点、终点、颜色、线宽
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# 画矩形
# 左上角、右下角
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# 填充矩形：thickness=-1
# cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), -1)

# 画圆
# 圆心、半径，填充：thickne=-1
cv2.circle(img, (447, 63), 64, (0, 0, 255), -1)

# 画椭圆
# 中心、轴、旋转角度、起始角度、结束角度，填充：thickne=-1
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 255, 0), -1)

# 画多边形
# 多边形点的坐标
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# -1代表默认：
pts = pts.reshape([-1, 1, 2])
cv2.polylines(img, [pts], True, (0, 255, 255))

# 写字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
