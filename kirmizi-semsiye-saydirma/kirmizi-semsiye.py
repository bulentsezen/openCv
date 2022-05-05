import cv2
import numpy as np
import imutils
 


# Grab the image

img = cv2.imread("foto.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

kirmizi_alt_deger = np.array([0,120,100])
kirmizi_ust_deger = np.array([10, 255, 255])

mask = cv2.inRange(hsv,kirmizi_alt_deger,kirmizi_ust_deger)

cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sayac = 0
for c in cnts:
    alan = cv2.contourArea(c)
    print('Alan:  ', alan)
    if alan > 1000: sayac += 1

    cv2.drawContours(img,[c],-1,(0,255,0),3)

print("Kırmızı şemsiye sayısı = ", sayac)

while True:
      cv2.imshow("Image", img)

      if cv2.waitKey(1) & 0xFF == ord('q'):
          break

