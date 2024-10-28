import cv2 as cv

#kameradan görüntü al
cap=cv.VideoCapture(0) #  0 default kamera, harici kamera için 1 degeri verilebilir.

while True:
    ret,frame=cap.read() #okunan her görüntüyü al
    
    cv.imshow("kamera",frame)
    if cv.waitKey(1) & 0xFF==ord("q"): #q tusuna basıldıktan sonra kamerayı kapat
        break

cap.relase()
cv.destroyAllwindows()
