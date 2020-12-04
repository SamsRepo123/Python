#Convert any image to cartoon
## MODULES REQUIRED ##
# opencv-python
# numpy

import cv2
import numpy as np

# reading libraries
img = cv2.imread("test.jpg")

# Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.medianBlur(gray, 9)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9 ,9)

# CARTOONING (CARTOON EFFECT)
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)


cv2.imshow("Image", img)
cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()