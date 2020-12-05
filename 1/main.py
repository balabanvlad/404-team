from PIL import Image

img = Image.open('best.bmp')

SizeX, SizeY = img.size

suma = 0

for i in range(1, SizeX):
    for j in range(1, SizeY):
        pixVal = img.getpixel((i, j))
        suma += pixVal[0]

print(suma)
