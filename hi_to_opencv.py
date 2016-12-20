import cv2
import numpy as np

img = cv2.imread('dummy/test1.png')
cv2.imshow('test image', cv2.resize(img, (960, 540))  )

edge = cv2.Canny(img,100,200)
cv2.imshow('edge', cv2.resize(edge, (960, 540)))
kernel = np.ones((6, 6), np.uint8)
closing = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closing', cv2.resize(closing, (960, 540)))
h, w = closing.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

# cv2.floodFill(closing, mask, (0,0), 255)
# cv2.imshow('floodFill', closing)
_,contour,_ = cv2.findContours(closing,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contour:
    cv2.drawContours(closing,[cnt],0,255,-1)

res = cv2.bitwise_not(closing)
cv2.imshow('gray',cv2.resize(np.invert(res), (960, 540)) )
cv2.waitKey(0)