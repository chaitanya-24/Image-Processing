import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('butterfly.jpg', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)

dilated_image = cv2.dilate(image, kernel, iterations=3)

eroded_image = cv2.erode(image, kernel, iterations=3)

opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

gradient_image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

tophat_image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

blackhat_image = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

plt.figure(figsize=(12, 8))

plt.subplot(3, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(3, 3, 2), plt.imshow(dilated_image, cmap='gray'), plt.title('Dilation')
plt.subplot(3, 3, 3), plt.imshow(eroded_image, cmap='gray'), plt.title('Erosion')
plt.subplot(3, 3, 4), plt.imshow(opened_image, cmap='gray'), plt.title('Opening')
plt.subplot(3, 3, 5), plt.imshow(closed_image, cmap='gray'), plt.title('Closing')
plt.subplot(3, 3, 6), plt.imshow(gradient_image, cmap='gray'), plt.title('Gradient')
plt.subplot(3, 3, 7), plt.imshow(tophat_image, cmap='gray'), plt.title('Top Hat')
plt.subplot(3, 3, 8), plt.imshow(blackhat_image, cmap='gray'), plt.title('Black Hat')

plt.show()
