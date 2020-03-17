# ångstromCTF
## 2020
### Reasonably Secure Algorithm

It looks like a simple RSA challenge. Using [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool),
and writing a script,
```shell script
#!/bin/bash

./RsaCtfTool/RsaCtfTool.py --createpub -n 126390312099294739294606157407778835887 -e > pubkey.pub
./RsaCtfTool/RsaCtfTool.py --publickey ./pubkey.pub --uncipher 13612260682947644362892911986815626931
```
gives the flag.

---
Flag: `actf{10minutes}`