
import cv2
import numpy as np


img1 = cv2.imread("thor.jpg")
img1 = cv2.resize(img1,(1000,600))

 
brdr = cv2.copyMakeBorder(img1,20,20,10,10,cv2.BORDER_CONSTANT,value = [255,0,125])

cv2.imshow("res",brdr)
cv2.waitKey(0)
cv2.destroyAllWindows()
