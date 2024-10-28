import cv2 as cv
import numpy as np


#Giriş ve çıkış video 
input_video="data/araba.mp4"
output_video="data/araba_renk.mp4"


#Video yakala

cap=cv.VideoCapture(input_video)

#Video özelliklerine bak

fourcc=cv.VideoWriter_fourcc(*"mp4v")
fps=cap.get(cv.CAP_PROP_FPS)
width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH)) #genişlik
height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)) #yükseklik
#kodek=cap.get(cv.CAP_PROP_FOURCC)


out=cv.VideoWriter(output_video,fourcc,fps,(width,height)) #videomuzu belirtilen özelliklerde oluşturur.

while cap.isOpened():
    ret,frame=cap.read() #okunan her görüntüyü al

    if not ret: #okuma başarılı ise
        break


    #renk kanallarını ayarla
    b,g,r=cv.split(frame)

    rgb_frame=cv.merge((b,r,r))
    cv.imshow("Sarı video",rgb_frame)

    out.write(rgb_frame)
    if cv.waitkey(1) & 0xFF==ord("q"): #q ya basıldığında kapatır
        break   



cap.release()
out.release()
cv.destroyAllWindows(0)