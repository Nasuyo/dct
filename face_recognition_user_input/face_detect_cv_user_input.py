import cv2
import sys
import numpy as np

# Functions ---------------------------------------------------------------
def mouse_callback(event, x, y, flags, param):
    global image_to_show, s_x, s_y, e_x, e_y, mouse_pressed
    
    smoothing = 50
    kernel = np.ones((smoothing, smoothing))/smoothing/smoothing

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
        dst = cv2.filter2D(image[s_y:y, s_x:x, :], -1, kernel)
        image[s_y:y, s_x:x] = dst  
        image_to_show = np.copy(image)      

# Get user supplied values ------------------------------------------------
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

# User input -----------------------------------------------------------------
# shrink the image so it fits the screen when asking for user input
width = int(image.shape[1]*0.2)
height = int(image.shape[0]*0.2)
image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# image_to_show is the one that is displayed, image is the one that is edited.
# Whenever you see changes in the image displayed, it is because image_to_show was newly assigned
image_to_show = np.copy(image)

mouse_pressed = False
s_x = s_y = e_x = e_y = -1

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('image', image_to_show)
    k = cv2.waitKey(1)

    if k == ord('c'):  # stop
    	break           
    elif k == ord('s'):  # save
        image_to_show = np.copy(image)
        cv2.imwrite("output_user1.png", image_to_show)
    elif k == ord('r'):  # reload
        image_to_show = np.copy(image)
    elif k == 27:
        break

cv2.destroyAllWindows()

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
width = int(image.shape[1]*0.2)
height = int(image.shape[0]*0.2)
image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

image_to_show = np.copy(image)

mouse_pressed = False
s_x = s_y = e_x = e_y = -1

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('image', image_to_show)
    k = cv2.waitKey(1)

    if k == ord('c'):  # stop
    	break           
    elif k == ord('s'):  # save
        image_to_show = np.copy(image)
        cv2.imwrite("output_user2.png", image_to_show)
    elif k == 27:
        break

cv2.destroyAllWindows()
