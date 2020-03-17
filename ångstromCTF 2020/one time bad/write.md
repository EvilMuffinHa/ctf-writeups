# ångstromCTF
## 2020
### one time bad

The [source](chall.py) code for this challenge seems to use OTP to encrypt the message.  
Looking at it closely, it uses `time.time()` as a seed for the randomness. After creating a [script](crack.py) that runs the 
program twice quickly in succession and running this script a few times, the flag is printed out.

---
Flag: `actf{one_time_pad_more_like_i_dont_like_crypto-1982309}`