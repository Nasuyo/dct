import cv2
import sys
import numpy as np

# Get user supplied values
imagePath1 = "im1.jpg"
imagePath2 = "im2.jpg"
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image 1 --------------------------------------------------------
image = cv2.imread(imagePath1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,  # works on the gray scale image
    scaleFactor=1.31,  # compensates for some faces being closer to the camera than others
    minNeighbors=1,  # defines how many objects are found near the current one before declaration
    minSize=(200, 200)  # minimum size of the window
)

print("Found {0} faces!".format(len(faces)))

# Blur the faces
smoothing = 150  # the larger the number the more intense is the blurring
kernel = np.ones((smoothing, smoothing))/smoothing/smoothing
for (x, y, w, h) in faces:
    dst = cv2.filter2D(image[y:y+h, x:x+w, :], -1, kernel)
    image[y:y+h, x:x+w] = dst

cv2.imwrite("output1.jpg", image)

# Read the image 2 ----------------------------------------------------------
image = cv2.imread(imagePath2)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.17,
    minNeighbors=4,
    minSize=(70, 70)
)

print("Found {0} faces!".format(len(faces)))

# Blur the faces
smoothing = 150
kernel = np.ones((smoothing, smoothing))/smoothing/smoothing
for (x, y, w, h) in faces:
    dst = cv2.filter2D(image[y:y+h, x:x+w, :], -1, kernel)
    image[y:y+h, x:x+w] = dst
    
cv2.imwrite("output2.jpg", image)

# User input -----------------------------------------------------------------
image_to_show = np.copy(image)
mouse_pressed = False
s_x = s_y = e_x = e_y = -1

def mouse_callback(event, x, y, flags, param):
    global image_to_show, s_x, s_y, e_x, e_y, mouse_pressed

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        s_x, s_y = x, y
        image_to_show = np.copy(image)

    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            image_to_show = np.copy(image)
            cv2.rectangle(image_to_show, (s_x, s_y),
                          (x, y), (0, 255, 0), 1)

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        e_x, e_y = x, y
        
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('image', image_to_show)
    k = cv2.waitKey(1)

    if k == ord('c'):
        if s_y > e_y:
            s_y, e_y = e_y, s_y
        if s_x > e_x:
            s_x, e_x = e_x, s_x

        if e_y - s_y > 1 and e_x - s_x > 0:
            image = image[s_y:e_y, s_x:e_x]
            image_to_show = np.copy(image)
    elif k == 27:
        break

cv2.destroyAllWindows()
