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
    gray,
    scaleFactor=1.31,
    minNeighbors=1,
    minSize=(200, 200)
)

print("Found {0} faces!".format(len(faces)))

# Blur the faces
smoothing = 150
kernel = np.ones((smoothing, smoothing))/smoothing/smoothing
for (x, y, w, h) in faces:
#    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#    print(x, y, w, h)
#    print(np.shape(image[y:y+h, x:x+w]))
#    dst = cv2.GaussianBlur(image[y:y+h, x:x+w, :], (smoothing, smoothing), 0)
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
