
import cv2
import numpy as np
 
image = cv2.imread("C:/Users/Downloads/3.jpg")
print(image.shape) # Print image shape
cv2.imshow("original", image)
imageCopy = image.copy()

cv2.circle(imageCopy, (100, 100), 30, (255, 0, 0), -1)
 
cv2.imshow('image', image)
cv2.imshow('image copy', imageCopy)
 
# Cropping an image
cropped_image = image[80:280, 150:330]
 
# Display cropped image
cv2.imshow("cropped", cropped_image)
 
# Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
