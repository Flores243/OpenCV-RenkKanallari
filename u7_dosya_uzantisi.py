import cv2 as cv

img=cv.imread("data/satranc3x3.jpg")

b,g,r=cv.split(img)

mavi_img=cv.merge((r,g,b))


cv.imshow("Mavi dama",mavi_img)
cv.imwrite(r"data/mavi_dama.jpg",mavi_img)
cv.waitKey(0)
cv.destroyAllWindows()
