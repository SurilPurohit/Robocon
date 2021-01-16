import cv2
import numpy as np

image = cv2.imread('watch.jpg')

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower_red = np.array([178,179,0])
upper_red = np.array([255,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)

cv2.imshow("O image",image)
cv2.imshow("C Detection",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
