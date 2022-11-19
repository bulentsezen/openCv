from PIL import Image
import os

size_300 = (300,300)

for f in os.listdir("."):
    if f.endswith(".jpg") or f.endswith(".JPG"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail((size_300))
        i.save("300/{}_300{}".format(fn,fext))

