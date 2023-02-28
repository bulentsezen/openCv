import cv2
import os

path = 'C:/Users/bseze/PycharmProjects/yolov8_3_8/Resimler/'

pre_imgs = os.listdir(path)
print(pre_imgs)
img = []

for i in pre_imgs:
    i = path+i
    # print(i)
    img.append(i)

print(img)

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

frame = cv2.imread(img[0])
size = list(frame.shape)
del size[2]
size.reverse()
# print(size)

video = cv2.VideoWriter("uretilen_video.mp4", cv2_fourcc, 24, size) #output video name, fourcc, fps, size

for i in range(len(img)):
    video.write(cv2.imread(img[i]))
    print('frame ', i+1, ' of ', len(img))

video.release()
print('üretilen video kaydedildi.')
