import cv2

cap = cv2.VideoCapture("ucus1_Trim.mp4")

# eğer 1 ile başlatırsak 10 dan sonra 100 e geçiyor, sıralama yanlış oluyor
sayac = 10000

while True:
    success, img = cap.read()
    outfile = 'Resimler/resim_%s.jpg' % (sayac)
    sayac += 1
    print(outfile)
    cv2.imwrite(outfile, img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

