# For reading images we have to know about the imread function of OpenCV
# Just write cv2.imread for reading image  

import cv2
import numpy as numpy
import matplotlib.pyplot as plt

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  
plt.show()
