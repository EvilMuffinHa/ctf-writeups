# ångstromCTF
## 2020
### Lo-Kee
###### [Back](../write.md)

Lo Kee provides us with [a'wa, w, and b'wb](chall.txt) in the Ko-Lee key exchange. After fiddling around with the rubiks
cube scrambles, we see that a'wa only affects the corners when compared to w, and b'wb only affects the edges.
By combining the corners from a'wa and the edges from b'wb, we get a'b'wba. Then, solving it using the [link](https://rubiks-cube-solver.com/) provided
in the challenge, we get F2D'F2UL2B2UR2UL2B'R'BLD'R2F'D2B2R'.

---
Flag: `actf{F2D'F2UL2B2UR2UL2B'R'BLD'R2F'D2B2R'}` 