import cv2
import numpy as np

def nothing(x):
   pass

cap=cv2.VideoCapture(0)

cv2.namedWindow("frame")

cv2.createTrackbar("test","frame",50,500,nothing)
cv2.createTrackbar("color/gray")
while True:
    _,frame = cap.read()

    cv2.imshow("frame",frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
