#Apple password generator
import random

bum = "abcdefghijklmnopqrstuvwxyz0123456789"

psw = ""

for i in range(16):
	if i % 4 == 0 and i != 0:
		psw += '-'
	psw += random.choice(bum)

print("Password generated:\n" + psw)
