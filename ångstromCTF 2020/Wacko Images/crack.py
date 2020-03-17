from numpy import *
from PIL import Image

enc = Image.open(r"chall.png")
img = array(enc)

key = [41, 37, 23]

a, b, c = img.shape

for x in range (0, a):
    for y in range (0, b):
        pixel = img[x, y]
        for i in range(0,3):
            for d in range(0, 8):
                if (pixel[i]+d*251)%key[i] == 0:
                    pixel[i]=int((pixel[i]+d*251)/key[i])
                    break
                else:
                    pass
        img[x][y] = pixel

dec = Image.fromarray(img)
dec.save('decrypt.png')
