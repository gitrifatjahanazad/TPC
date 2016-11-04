import cv2

img = cv2.imread('dummy/test3.png')
cv2.imshow('test image',img)

edge = cv2.Canny(img,100,200)
cv2.imshow('edge',edge)

cv2.waitKey(0)