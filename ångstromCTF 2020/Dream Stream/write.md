# ångstromCTF
## 2020
### Dream Stream

If we set the key equal to the golden ratio, `(1 - sqrt(5))/2`, then because the `keystream` function raises
the key to an odd number. `phi^n` gets closer to an integer as `n` increases. Since `(1 - sqrt(5))/2` is negative, 
`((1 + sqrt(5)) / 2 ) ^ n` goes above and below `0` as `n` increases. This means that the keystream will either be 
`101010101010...` or `01010101010...`. Trying out both reveals that the key is `01010101010...` and the first part of the flag.  
Because of floating point numbers, precision problems occur, so decoding the string without `XOR`ing it with the key reveals the 
last part of the flag. The letter `o` was cut off in the middle, but it is clearly `o` once the flag is revealed.

---
Flag: `actf{it_hurt_itself_in_its_confusion}`