import cv2 as cv

#Dosya oku 
img=cv.imread("data/kizil_sac3.jpg")
img_fer=cv.imread("data/ferrari.jpg")
img_togg=cv.imread("data/togg.jpg")

b,g,r=cv.split(img)
bf,gf,rf=cv.split(img_fer)
bf,gf,rf=cv.split(img_togg)


#mavi saç
img_mavi=cv.merge((r,g,b))

#mavi ferrari

mv_fer=cv.merge((rf,gf,bf))


#sarı saç
sari_sac2=cv.merge((b,r,r))


#laci ferrari
lc_ferrari=cv.merge((rf,gf,gf))

#pembe ferrari
pb_ferrari=cv.merge((rf,gf,rf))

#Turkuaz
tr_fer=cv.merge((rf,rf,bf))

#togg
img_togg=cv.merge((rf,rf,bf))

#fotoyu göster
cv.imshow("Orijinal saç",img)
cv.imshow("Mavi saç",img_mavi)
cv.imshow("Sarı saç",sari_sac2)

cv.imshow("kırmızı ferrari",img_fer)
cv.imshow("mavi ferrari",mv_fer)
cv.imshow("laci ferrari",lc_ferrari)
cv.imshow("pembe ferrari",pb_ferrari)
cv.imshow("turkuaz ferrari",tr_fer)
cv.imshow("togg",img_togg)


cv.waitKey(0)
cv.destroyAllWindows()
