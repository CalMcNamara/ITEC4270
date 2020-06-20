import numpy as np
import cv2

im = cv2.imread('colors.png')
print(type(im))

hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)

lower_range = np.array([100,50,50])
upper_range = np.array([130,255,255])

mask = cv2.inRange(hsv,lower_range,upper_range)

cv2.imshow('image',im)
cv2.imshow('mask',mask)

while(True):
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()