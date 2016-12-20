import cv2
import numpy as np

img = cv2.imread('dummy/1-fp.png')
cv2.imshow('test image', cv2.resize(img, (960, 540))  )

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imshow('blurred',cv2.resize(np.invert(blurred), (960, 540)) )
edge = cv2.Canny(blurred,10,200)
cv2.imwrite('canny.png', cv2.resize(edge, (960, 540)))
cv2.waitKey(0)