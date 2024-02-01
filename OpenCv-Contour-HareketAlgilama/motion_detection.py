import cv2
import numpy as np

cap = cv2.VideoCapture('cctv_trafik.mp4')

while cap.isOpened():
    ret, frame1 = cap.read()

    cv2.imshow("feed", frame1)

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()