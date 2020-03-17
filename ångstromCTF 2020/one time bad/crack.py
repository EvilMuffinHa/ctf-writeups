import os
with open('results.txt', 'w') as f:
    f.write('')

os.system("printf '2\n" + 'k' + "' | nc misc.2020.chall.actf.co 20301 > results.txt")
with open('results.txt', 'r') as f:
    os.system("printf '2\n" + f.read().split(' ')[73] + "' | nc misc.2020.chall.actf.co 20301")
