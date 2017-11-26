# 模板匹配示例
# ex2tron 22017年11月14日
# http://ex2tron.top
# 官方python-opencv文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('material/lena.jpg', 0)
template = cv2.imread('material/lena-template.jpg', 0)
w, h = template.shape[::-1]
# 相当于下面这句：
# h, w = template.shape

# 6种模板匹配方法
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img2 = img.copy()
    method = eval(meth)

    # 模板匹配
    res = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # 如果匹配方式是TM_SQDIFF/TM_SQDIFF_NORMED左上角取min_loc
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img2, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img2, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
