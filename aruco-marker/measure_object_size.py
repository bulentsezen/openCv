### pip install opencv-contrib-python

import cv2
from object_detector import *
import numpy as np

# Load Aruco detector
parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)   ### 5cm - 5cm aruco marker


# Load Object Detector
detector = HomogeneousBgDetector()

# Load Image
img = cv2.imread("resim-1.jpg")

# Get Aruco marker
corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

# Draw polygon around the marker
int_corners = np.int0(corners)    ### köşe noktaların koordinatları tamsayı olmak zorunda
cv2.polylines(img, int_corners, True, (0, 255, 0), 5)   ### aruco marker etrafına yeşil çizgi çiziyoruz.  

# Aruco Perimeter (aruco marker çevre uzunluğu)
aruco_perimeter = cv2.arcLength(corners[0], True)

# Pixel to cm ratio  (pixel sayısını cm ye çeviren oran)
pixel_cm_ratio = aruco_perimeter / 20     ### aruco marker 5cm olduğu için çevre toplamı 20cm eder.

contours = detector.detect_objects(img)

# Draw objects boundaries
for cnt in contours:
    # Get rect
    rect = cv2.minAreaRect(cnt)   ### nesnenin etrafını çevreleyen minimum diktörtgen alanı koordinatlarını, genişlik ve uzunluğunu ve açısını verir
    (x, y), (w, h), angle = rect

    # Get Width and Height of the Objects by applying the Ratio pixel to cm
    object_width = w / pixel_cm_ratio
    object_height = h / pixel_cm_ratio

    # Display rectangle
    box = cv2.boxPoints(rect)
    box = np.int0(box)       ### köşe nokta koordinatları tamsayı olmak zorunda
 
    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)     ###  algılanan nesnelerin merkez noktasında çizilen çemberin içini (-1 değeri ile) girilen renkle (kırmızı) doldurur.
    cv2.polylines(img, [box], True, (255, 0, 0), 2)           ###  algılanan nesnelerin etrafında mavi renkli dikdörtgen çizer
    cv2.putText(img, "Genislik {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    cv2.putText(img, "Uzunluk {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
 


cv2.imshow("Image", img)
cv2.waitKey(0)
