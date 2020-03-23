# NACTF
## 2019
### Super Duper AES
###### [Back](../write.md)

Looking at the [source](sdaes.py) and the challenge, the SP network doesn't seem to have a key.
Therefore, just reversing the process by first unpermuting the permutation and then unsubsitituting the 
substitution 10000 times will retrieve the flag. After trying out different values for the `permutation` function,
we see that the permutation function checks whether a bit equal to `1`, and then changes its position based on
the array. Then, after putting together the `unpermute` and `unsubstitute` functions in a python [file](crack.py)
and running it, the flag is retrieved.

---
Flag: `nactf{5ub5t1tut10n_p3rmutat10n_n33d5_a_k3y}`