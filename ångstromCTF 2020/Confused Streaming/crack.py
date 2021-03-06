import binascii

# By fiddling around with the program, we see that the ciphertext always remains the same if the key is between 0 and 1
stream = "01100001011000110111010001100110011110110110010001101111011101110110111001011111011101000110111101011111011101000110100001100101010111110110010001100101011000110110100101101101011000010110110001111101 "
# Now just convert the cipher text to ascii
y = int(stream, 2)
z = hex(y)
print(binascii.unhexlify(bytes(z[2:].encode())))

