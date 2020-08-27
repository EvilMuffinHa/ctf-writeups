with open('chall.txt', 'r') as f:
    c = f.read()

c = c.split(' ')
for i in c:
    if len(str(i)) != 8:
        print(chr(int(i) + 18))
    else:
        pass