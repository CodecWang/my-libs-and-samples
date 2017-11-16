# 打开图片、保存图片
# ex2tron 22017年11月13日
# http://ex2tron.top
# 官方文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#display-image


import cv2

image = cv2.imread("material/lena.jpg")
# 灰度图加载
# image = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('original', image)
cv2.imshow('GRAY', img2gray)

# 或者，先定义窗口，可指定窗口大小：
# cv2.namedWindow('original', cv2.WINDOW_NORMAL)
# cv2.imshow('original', image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 或者
k = cv2.waitKey(0)
if(k == 27):
    cv2.destroyAllWindows()
# 保存图片
elif(k == ord('s')):
    cv2.imwrite('savedlena.jpg', image)
    cv2.destroyAllWindows()
