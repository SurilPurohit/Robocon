import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
   pass

cv2.namedWindow('colourbars')

hh='Max'
hl='Min'
wnd='colorbars'

cv2.createTrackbar("Max","colorbars",0,255,nothing)
cv2.createTrackbar("Min","colorbars",0,255,nothing)

img=cv2.imread('watch.jpg',0)
img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)

while(1):
    hu1=cv2.getTrackbarPos("Max","colorbars")
    huh=cv2.getTrackbarPos("Min","colorbars")
    ret,thresh1=cv2.threshold(img,hu1,huh,cv2.THRESH_BINARY)
    ret,thresh2=cv2.threshold(img,hu1,huh,cv2.THRESH_BINARY_INV)
    ret,thresh3=cv2.threshold(img,hu1,huh,cv2.THRESH_TRUNC)
    ret,thresh4=cv2.threshold(img,hu1,huh,cv2.THRESH_TOZERO)
    ret,thresh5=cv2.threshold(img,hu1,huh,cv2.THRESH_TOZERO_INV)

    cv2.imshow("thresh1",thresh1)
    cv2.imshow("thresh2",thresh2)
    cv2.imshow("thresh3",thresh3)
    cv2.imshow("thresh4",thresh4)
    cv2.imshow("thresh5",thresh5)

    k=cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode=not mode
    elif k==27:
        break

cap.release()
cv2.destroyAllWindows()
