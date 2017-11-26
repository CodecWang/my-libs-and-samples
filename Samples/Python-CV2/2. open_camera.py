# 打开摄像头或本地视频
# ex2tron 2017年11月13日
# http://ex2tron.top
# 官方文档：
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html


import cv2

capture = cv2.VideoCapture(0)
# 播放本地视频
# capture = cv2.VideoCapture("material/demo_video.mp4")

# 获取视频的相关属性，如获取帧的宽、高
# 官方文档：
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html
print(capture.get(3))
print(capture.get(4))

# 设置视频的属性
capture.set(3, 320)
capture.set(4, 240)

while(True):
    ret, frame = capture.read()

    cv2.imshow('original', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)

    k = cv2.waitKey(30)
    if(k == ord('q')):
        break


capture.release()
cv2.destroyAllWindows()

# 录制视频：不常用，参考官方文档
