import cv2
from datetime import datetime
import streamlit as st

st.title("Motion Detector")
buttn = st.button("Start Camera")


if buttn:
    vso = cv2.VideoCapture(0)
    cam_img = st.image([])

    while True:
        time = datetime.now()
        check, frame = vso.read()
        new = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.putText(img=new, text= time.strftime("%A"), org=(20, 20),fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2.5, color=(255, 0, 0), thickness=2, lineType= cv2.LINE_AA)
        cv2.putText(img=new, text=time.strftime("%b %d %Y, %I:%M:%S %p"), org=(20, 40), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2.5, color=(255, 0, 0), thickness=2, lineType= cv2.LINE_AA)
        cam_img.image(new)









