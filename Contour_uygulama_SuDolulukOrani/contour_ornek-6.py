import math
import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import imutils
 
# Initialize the Video
cap = cv2.VideoCapture('Videos/vid (4).mp4')

# Create the color Finder object
myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 8, 'smin': 106, 'vmin': 0, 'hmax': 15, 'smax': 255, 'vmax': 255}
 

while True:
    # Grab the image
 
    success, img = cap.read()
    #img = cv2.imread("Ball.png")
    img = img[0:900, :]
 
    # Find the Color Ball
    imgColor, mask = myColorFinder.update(img, hsvVals)
    # Find location of the Ball
    imgContours, contours = cvzone.findContours(img, mask, minArea=500)

    if contours:
        cx, cy = contours[0]['center']
        print(cx,cy)

    
    # Display
    imgContours = cv2.resize(imgContours, (0, 0), None, 0.7, 0.7)
    #cv2.imshow("Image", img)
    cv2.imshow("ImageColor", imgContours)
    cv2.waitKey(100)
