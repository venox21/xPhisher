from PIL import Image

img = Image.open("image.png")


img = img.resize((1024, 1024))


pixels = img.load()


pixels[100, 100] = (0, 0, 0)
pixels[200, 200] = (0, 0, 0)
pixels[300, 300] = (0, 0, 0)



img.save("oberhaupt.png")
print("oberhaupt")