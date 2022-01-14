import math
import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import imutils
 
# Initialize the Video
cap = cv2.VideoCapture('Videos/su_doldurma.mp4')

# Create the color Finder object
myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 34, 'smin': 20, 'vmin': 0, 'hmax': 119, 'smax': 255, 'vmax': 255}

hacim = 0

while True:
    # Grab the image
 
    success, img = cap.read()
    #img = cv2.imread("su.png")
    img = img[0:500, :]
 
    # Suyun rengini bul
    imgColor, mask = myColorFinder.update(img, hsvVals)
    # Suyun olduğu yerleri bul
    imgContours, contours = cvzone.findContours(img, mask, minArea=500)

    # Suyun toplam hacmini bul
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        area = cv2.contourArea(c)
        hacim = hacim + area
        if hacim < 12100000:
            #print('Doluluk oranı:  ', hacim/12000000*100)
            cv2.putText(imgContours, f'Doluluk: %{str(int(hacim/12000000*100))}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 0), 3)

        #print(area)

    
    
    # Display
    imgContours = cv2.resize(imgContours, (0, 0), None, 0.7, 0.7)
    #cv2.imshow("Image", img)
    cv2.imshow("ImageColor", imgContours)
    cv2.waitKey(100)
