from PIL import Image

img = Image.open('best.bmp')

SizeX, SizeY = img.size
suma = 0
k = 0
for i in range(0, SizeX):
    for j in range(0, SizeY):
        k+=1
        pixVal = img.getpixel((i, j))
        suma += pixVal[0]

print(suma)
