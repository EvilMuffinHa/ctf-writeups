# ångstromCTF
## 2020
### Discrete Superlog
###### [Back](../write.md)

Challenge:
```
We define a^^b to be such that a^^0 = 1 and a^^b = a^(a^^(b-1)), where x^y represents x to the power of y.
Given this, find a positive integer x such that a^^x = b mod p.
```

By looking up `modular tetration`, there is an article about the math behind calculating this. 
There is also a script for this online, and by using this script, the flag is given.

---
Flag: `actf{lets_stick_to_discrete_log_for_now...}`