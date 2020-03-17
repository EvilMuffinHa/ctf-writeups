# nc crypto.2020.chall.actf.co 20601

from __future__ import print_function
import random,os,sys,binascii
from decimal import *
try:
	input = raw_input
except:
	pass
getcontext().prec = 1000
def keystream(key):
	random.seed(int(os.environ["seed"])) #predicting a specific random number
	e = random.randint(100,1000) # kinda random but same every time, probably for multiple people ctf purposes
	while 1:
		d = random.randint(1,100) #Without seed
		ret = Decimal('0.'+str(key ** e).split('.')[-1]) # Multiplying the key by "e", which is the pseudo random number with seed
		for i in range(d): #multiplying it by a random power of 2
			ret*=2
		yield int((ret//1)%2) # Returning a number which is either 0 or 1 from that by checking whether the integer part is even or not.
		e+=1 #Increment E
try:
	a = int(input("a: "))
	b = int(input("b: "))
	c = int(input("c: "))
	# remove those pesky imaginary numbers, rationals, zeroes, integers, big numbers, etc
	if b*b < 4*a*c or a==0 or b==0 or c==0 or Decimal(b*b-4*a*c).sqrt().to_integral_value()**2==b*b-4*a*c or abs(a)>1000 or abs(b)>1000 or abs(c)>1000:
		raise Exception()
	key = (Decimal(b*b-4*a*c).sqrt() - Decimal(b))/Decimal(a*2) # If it isn't rational, the key is a decimal which is using the quad form
except:
	print("bad key")
else:
	flag = binascii.hexlify(os.environ["flag"].encode())
	flag = bin(int(flag,16))[2:].zfill(len(flag)*4)
	ret = ""
	k = keystream(key)
	for i in flag:
		ret += str(next(k)^int(i)) # XORing the every value in the keystream with every value in the flag
	print(ret)