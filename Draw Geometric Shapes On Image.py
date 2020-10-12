# Importing Relevent Libraries
import cv2
import numpy as np

# Create a Black image using NumPy 
img = np.zeros([512, 512, 3], np.uint8)

# Create a Line on Image 
""" Arguement :
1. Matrics of Image
2. Co-ordinate of Point 1
3. Co-ordinate of Point 2
4. Color of Line
5. Thickness of the shape 
"""
img = cv2.line(img, (345, 0), (255, 255), (255, 0, 0), 5)
""" Arrowed Line is same as Line Shape
"""
img = cv2.arrowedLine(img, (0, 0), (255, 255), (255, 0, 0), 5)
""" We have to make first font of the text I want to text on image"""

# Make Rectangle
img = cv2.rectangle(img, (348, 0), (510, 128), (255, 0, 0), 5)

# Make Circle
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
""" Arguements
1. matrix of Image
2. Text 
3. Points
4. Font 
5. Font Size
6. Color
7. Thickness
8. Line text or what
"""
img = cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA) 

# Display image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

""" And Many more Shapes have OpenCV. """