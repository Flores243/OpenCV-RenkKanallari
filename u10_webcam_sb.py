import cv2 as cv

#kamerayı başlat 
cap=cv.VideoCapture(0)

while True:
    ret,frame=cap.read() #okunan her görüntüyü al
    
    cv.imshow("kamera",frame)
    if not ret: 
        break
    #gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    hvs_img=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    #cv.imshow("gray",gray_frame)
    cv.imshow("gray",hvs_img)
    
    
    if cv.waitKey(1) & 0xFF==ord("q"): #q tusuna basıldıktan sonra kamerayı kapat
        break

#kamerayı kapat
cap.relase()
cv.destroyAllwindows()