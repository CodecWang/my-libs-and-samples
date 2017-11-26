# 图片的算术运算
# ex2tron 2017年11月21日
# http://ex2tron.top
# 官方文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html


import cv2
import numpy as np

# 图片相加
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))
print(x + y)  # 250+10 = 260 % 256 = 4

# 图像混合，两张图片大小需一致
img1 = cv2.imread('material/m1.png')
img2 = cv2.imread('material/opencv_logo.png')
# 图片并排
ori = np.hstack((img1, img2))
dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('ori', ori)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 图片按位操作
img1 = cv2.imread('material/lena.jpg')
img2 = cv2.imread('material/opencv_logo.png')

# 创建ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# 反相图片
mask_inv = cv2.bitwise_not(mask)
# 或 mask_inv = 255 - mask

# 在ROI中抠出logo的区域
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
# 在logo原图中只抠出logo的部分
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('ori', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
