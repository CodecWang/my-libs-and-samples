import cv2

capture = cv2.VideoCapture(0)

ret, frame = capture.read()

while(True):
    ret, frame = capture.read()
    cv2.imshow('original', frame)
    k = cv2.waitKey(30)
    if(k == ord('c')):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
        image, contours, hierarchy = cv2.findContours(
            thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print(len(contours))
        # for i in range(len(contours)):
        #     cnt = contours[i]
        #     img = cv2.drawContours(thresh, [cnt], 0, (255, 0, 0), 3)
        #     cv2.imshow('contours', img)

        cnt = contours[0]


capture.release()
cv2.destroyAllWindows()
