from PIL import Image
import os

for f in os.listdir("."):
    if f.endswith(".jpg") or f.endswith(".JPG"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save("png/{}.png".format(fn))

# image1 = Image.open("mehmet.jpg")
# image1.save("mehmet.png")