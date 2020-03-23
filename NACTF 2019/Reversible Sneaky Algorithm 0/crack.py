import binascii
with open('chall.txt', 'r') as f:
    text = f.read()
n = int(text.split('\n')[0].split(': ')[-1])
d = int(text.split('\n')[1].split(': ')[-1])
c = int(text.split('\n')[2].split(': ')[-1])

p = pow(c, d, n)
z = hex(p)
print(binascii.unhexlify(bytes(z[2:].encode())).decode())