# 对图片的基本操作
# ex2tron 22017年11月13日
# http://ex2tron.top
# 官方python-opencv文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#basic-ops


import cv2

image = cv2.imread("material/lena.jpg")
cv2.imshow('original', image)

# 1.像素
print('px b-g-r value: ', image[100, 100])

# 2.属性
print('shape: ', image.shape)
print('image size: ', image.size)
print('data type: ', image.dtype)

# 3.ROI，使用numpy切片
roi = image[59:377, 82:427]
cv2.imshow('face roi', roi)

# 4.通道分割与合并
# 方式一：速度慢
b, g, r = cv2.split(image)
# 方式二：速度快
# b = image[:, :, 0]
# g = image[:, :, 1]
# r = image[:, :, 2]
cv2.imshow('blue channel', b)
cv2.imshow('green channel', g)
cv2.imshow('red channel', r)
# 合并：
img_merge = cv2.merge((b, g, r))
cv2.imshow('merge channel', img_merge)
cv2.waitKey(0)

# 5.加边框（不常用，可参考官方文档）
