from PIL import Image

image1 = Image.open("mehmet.jpg")
# image1.rotate(90).save("mehmet_yeni.jpg")

image1.convert(mode="L").save("mehmet_yeni.jpg")    # gri tona çevirir
