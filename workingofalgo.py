import cv2
import time

vdo = cv2.VideoCapture(0)
time.sleep(1)
first_frame=None

while True:
    check, frame = vdo.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gaussian_grey = cv2.GaussianBlur(grey, (21, 21), 0)
    cv2.imshow("vd", gaussian_grey)
    if first_frame is None:
        first_frame = gaussian_grey
    imgdif= cv2.absdiff(first_frame, gaussian_grey)
    thres=cv2.threshold(imgdif, 60, 255, cv2.THRESH_BINARY)[1]
    final=cv2.dilate(thres, None, iterations=2)
    # cv2.imshow("vd", final)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

vdo.release()