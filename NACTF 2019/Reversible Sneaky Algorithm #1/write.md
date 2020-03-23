# NACTF
## 2019
### Reversible Sneaky Algorithm #1
###### [Back](../write.md)

The challenge says that the flag is only 4 letters long, `n` is too large to factor, and `e` is pretty secure as 
it is `65537`. This indicates that we should brute force the flag. Brute forcing it using [this script](crack.py)
gives us the flag.
---
Flag: `nactf{pkcs}`