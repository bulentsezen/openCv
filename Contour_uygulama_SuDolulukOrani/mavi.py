import cv2
import numpy as np
import cvzone
#from cvzone.ColorModule import ColorFinder
import imutils
 

while True:
    # Grab the image
 
    #success, img = cap.read()
    img = cv2.imread("mavi.png")

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mavi_alt_deger = np.array([90,60,0])
    mavi_ust_deger = np.array([121, 255, 255])

    mask = cv2.inRange(hsv,mavi_alt_deger,mavi_ust_deger)

    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        alan = cv2.contourArea(c)
        print('Alan:  ', alan)

        cv2.drawContours(img,[c],-1,(0,255,0),3)



    key = cv2.waitKey(1)
    if key == 27:
        break

    cv2.imshow("Image", img)
    cv2.waitKey(1)
