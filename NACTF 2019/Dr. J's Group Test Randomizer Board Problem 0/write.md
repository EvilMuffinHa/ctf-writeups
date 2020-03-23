# NACTF
## 2019
### Dr. J's Group Test Randomizer: Board Problem #0
###### [Back](../write.md)

The challenge asks us to give two answers to the random number generator. Looking at the [code](chall.c), 
we see that the random function uses the previous random number as a seed.  
```c
uint64_t nextRand() {
  // Keep the 8 middle digits from 5 to 12 (inclusive) and square.
  seed = getDigits(seed, 5, 12);
  seed *= seed;
  return seed;
}
```
After writing a simple [script](crack.py) to generate new random numbers based on old ones and plugging in the values,
the program reveals the flag.

---
Flag: `nactf{1_l0v3_chunky_7urn1p5}`