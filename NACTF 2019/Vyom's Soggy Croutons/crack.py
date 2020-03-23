
chall = 'ertkw{vk_kl_silkv}'
for a in range(26):
    dec = ''
    for i in chall:
        if 122 >= ord(i) >= 97:
            dec += chr((ord(i)-97+a)%26 + 97)
        else:
            dec += i
    print(dec)