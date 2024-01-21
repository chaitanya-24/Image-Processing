import cv2
import numpy as np


img = cv2.imread('butterfly.jpg')
img = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)
img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gradients_sobelx = cv2.Sobel(img, -1, 1, 0)
gradients_sobely = cv2.Sobel(img, -1, 0, 1)
gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5, gradients_sobely, 0.5, 0)

gradients_laplacian = cv2.Laplacian(img, -1)

canny_output = cv2.Canny(img, 80, 160)

cv2.imshow('Sobel x', gradients_sobelx)
cv2.imshow('Sobel y', gradients_sobely)
cv2.imshow('Sobel X+y', gradients_sobelxy)
cv2.imshow('laplacian', gradients_laplacian)
cv2.imshow('Canny', canny_output)
cv2.waitKey()