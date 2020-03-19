# (1 + sqrt(5))/2 gives a key of 0101010101010...
# because ((1 + sqrt(5))/2) ^ n + ((1-sqrt(5))/2) ^n will give an integer as the sqrt(5)'s cancel out.
import binascii

stream = '11001011110010011101111011001100110100011100001111011110111101011100001011011111110110001101111011110101110000111101111011011001110011111100011011001100111101011100001111000100111101011100001111011110110110011111010111001001110011110110111001100110011101010111001101101001011011110110111001111101'
ret = ''
a = 1
for i in stream:
    if a%2==0:
        ret += i
    else:
        ret += str(1^int(i))
    a+=1


y = int(ret, 2)
z = hex(y)
print(binascii.unhexlify(bytes(z[2:].encode())))

ret = ''
a = 1
for i in stream:
    if a%2==0:
        ret += i
    else:
        ret += i
    a+=1


y = int(ret, 2)
z = hex(y)
print(binascii.unhexlify(bytes(z[2:].encode())))



