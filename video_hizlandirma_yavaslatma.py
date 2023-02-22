import cv2

cap = cv2.VideoCapture("su_doldurma.mp4")

# video kayıt için fourcc ve VideoWriter tanımlama
cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')
success, img = cap.read()
size = list(img.shape)
del size[2]
size.reverse()
video = cv2.VideoWriter("hizli_video.mp4", cv2_fourcc, 220, size) #output video name, fourcc, fps, size

while True:
    success, img = cap.read()
    video.write(img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

video.release()