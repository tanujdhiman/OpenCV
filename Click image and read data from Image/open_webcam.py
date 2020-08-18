import cv2

cap = cv2.VideoCapture(0) #starting video capturing

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam") #raise this error

while True:   # do running this loop 
    ret, frame = cap.read() 
    frame = cv2.resize(frame, (0, 0), fx=1, fy=1, interpolation=cv2.INTER_LINEAR) #fx depends on width
    # fy depends on height
    # interpolation is used for resizing and shriking.
    # Parameters : 
    # 1. inter_area : shrink an image
    # 2. inter_cubic : this is slow but more efficient
    # 3. inter_linear : when zooming is required
    cv2.imshow('Frame', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()

#Just press ESC key for stopping the web cam using openCV