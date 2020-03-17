import math
from totient import totient


def towerMod(a, b, m):
    # base cases
    if m == 1:
        return 0
    if a == 1 or b == 0:
        return 1
    if b == 1:
        return a % m
    if a == m:
        return 0

    towerBiggerThanLog2m = checkTowerBiggerThanLogM(a, b - 1, math.log(m, 2))

    if towerBiggerThanLog2m:
        phiM = totient(m)  # or lambda(m)

        factorA = pow(a, phiM, m)
        factorB = pow(a, towerMod(a, b - 1, phiM), m)
        return (factorA * factorB) % m

    else:
        return pow(a, recursiveVal, m)

    pass


def checkTowerBiggerThanLogM(a, b, m):
    if a > round(m):
        return True
    if b == 1 or m <= 1:
        return a > round(m)

    return checkTowerBiggerThanLogA(a, b - 1, math.log(m, a))






while True:
    a = int(input("A: "))
    p = int(input("P: "))
    for x in range(20):
        print(towerMod(a, x+1, p), end=' ')
    print()
