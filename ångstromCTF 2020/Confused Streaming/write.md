# ångstromCTF
## 2020
### Confused Streaming

This challenge asks you for `a, b, and c` , forms a key using the roots of the equation `ax^2 + bx + c`, and uses a stream cipher to encrypt the flag.
By playing around with the `keystream` function in the [source](chall.py), if the key is between 0 and 1, it seems to always be a string of `0`'s.  
Since the flag is getting XORed with the key, decrypting the output automatically gives the flag.

---
Flag: `actf{down_to_the_decimal}`
