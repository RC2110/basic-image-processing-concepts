import cv2
import time
from sendemail import send_email
import glob
import os
from threading import  Thread

vdo = cv2.VideoCapture(0)
first_frame=None
deduct= []
numb=1

def del_img():
    print("delete folder function has started")
    lst =glob.glob("images/*.png")
    for i in lst:
        os.remove(i)
    print("delete folder function has completed")


while True:
    listvalue= 0
    check, frame = vdo.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gaussian_grey = cv2.GaussianBlur(grey, (21, 21), 0)
    if first_frame is None:
        first_frame = gaussian_grey
    imgdiff = cv2.absdiff(first_frame, gaussian_grey)
    thresh = cv2.threshold(imgdiff, 60, 255, cv2.THRESH_BINARY)[1]
    final = cv2.dilate(thresh, None, iterations=2)
    contours, chk = cv2.findContours(final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        if cv2.contourArea(i)<5000:
            continue # skips the remaining code inside the current iteration

        x,y,w,h = cv2.boundingRect(i)
        rect = cv2.rectangle(frame,(x,y),(w+x,h+y),(255,0,0), 2)
        if rect.any(): # these lines get executed only if area of contour is greater than 5000.
            listvalue = 1
            cv2.imwrite(f"images/{numb}.png", frame)
            numb = numb + 1
            lst = glob.glob("images/*.png")
            if len(lst)==1:
                imagepath=lst[0]
            else:
                midvalue = int((len(lst) + 1) / 2)
                imagepath = lst[midvalue]
            # print(imagepath)

    cv2.imshow("vd", frame)
    deduct.append(listvalue)
    value = deduct[-2:]


    if value[0]==1 and value [1]==0:
        email_thread = Thread(target=send_email, args=(imagepath,))
        email_thread.daemon=True # for running in the background
        email_thread.start()
        del_thread = Thread(target=del_img)
        # del_thread.daemon=True # for running in the background


    key = cv2.waitKey(1)
    if key == ord("q"):
        break
del_thread.daemon=True
del_thread.start()

vdo.release()



# cv2.imshow("vd", frame)