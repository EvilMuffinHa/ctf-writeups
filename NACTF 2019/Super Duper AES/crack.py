from binascii import unhexlify

def unsubstitute(hexBlock):
    unsubstitutedHexBlock = ''
    substitution = [15, 9, 7, 4, 1, 11, 6, 10, 0, 3, 13, 14, 12, 8, 5, 2]
    for hexDigit in hexBlock:
        newDigit = substitution[int(hexDigit, 16)]
        unsubstitutedHexBlock += hex(newDigit)[2:]
    return unsubstitutedHexBlock


def unpermute(hexBlock):
    unpermutation = [6, 22, 30, 18, 29, 4, 23, 19, 15, 1, 31, 11, 28, 14, 25, 2, 27, 12, 21, 26, 10, 16, 0, 24, 7, 5, 3,
                   20, 13, 9, 17, 8]
    sblock = ["0" for i in range(32)]
    for i in range(31, -1, -1):
        block = format(int(hexBlock, 16), "032b")

        if block[i] == "1":
            bit = unpermutation.index(31 - i)
            sblock[bit] = "1"

    sblock = "".join(sblock[::-1])

    return hexpad(hex(int(sblock, 2))[2:])


def hexpad(hexBlock):
    numZeros = 8 - len(hexBlock)
    return numZeros*"0" + hexBlock


def unround(hexMessage):
    numBlocks = len(hexMessage)//8
    unpermutedHexMessage = ""
    for i in range(numBlocks):
        unpermutedHexMessage += unpermute(hexMessage[8*i:8*i+8])
    unsubstitutedHexMessage = ""
    for i in range(numBlocks):
        unsubstitutedHexMessage += unsubstitute(unpermutedHexMessage[8*i:8*i+8])
    return unsubstitutedHexMessage

hexMessage = 'd59fd3f37182486a44231de4713131d20324fbfe80e91ae48658ba707cb84841972305fc3e0111c753733cf2'
for i in range(10000):
    hexMessage = unround(hexMessage)


print(unhexlify(hexMessage).decode('utf-8'))