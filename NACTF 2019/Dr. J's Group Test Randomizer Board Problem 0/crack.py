def crack(randnum):
    return int(str(randnum)[4:12]) ** 2




z = int(input('Num: '))

for i in range(10):
    z = crack(z)
    print(z)