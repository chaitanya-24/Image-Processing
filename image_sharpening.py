import cv2
import numpy as np

img = cv2.imread('butterfly.jpg')
img = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)

gaussian_blur = cv2.GaussianBlur(img, (7,7), 2)

sharpened1 = cv2.addWeighted(img,1.5, gaussian_blur, -0.5, 0)
sharpened2 = cv2.addWeighted(img,3.5, gaussian_blur, -2.5, 0)
sharpened3 = cv2.addWeighted(img,7.5, gaussian_blur, -6.5, 0)

cv2.imshow('Sharpened 3', sharpened3)
cv2.imshow('Sharpened 2', sharpened2)
cv2.imshow('Sharpened 1', sharpened1)
cv2.imshow('original', img)
cv2.waitKey(0)