# ångstromCTF
## 2020
### Wacko Images
The challenge includes a [source](chall.py) and an image.  

![Challenge Image](chall.png)

Looking at the source, the encryption involves multiplying each pixel by its corresponding key
 (mod 251):  
 `pixel[i] * key[i] % 251`.  
To deal with the mod, I used a for loop and checked whether `(pixel[i]+x*251)%key[i]` was equal to 0 for  
values of `x` from 1 through 8. My full code:
```python
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
```
This reveals a message in the image:  
![Image of Decrypted picture](decrypt.png)

---
Flag: `actf{m0dd1ng_sk1llz}`