#wordle by Adam Jones for Python 2 | v1.0 12/8/2023 | UPDATED to v2.0 1/1/2024

import random

#COLORS
GREEN = '\033[42m'
RED = '\033[41m'
YELLOW = '\033[43m'
ENDC = '\033[0m'

#REWORKED GUESS FUNCTION
def guess(word, solution):
	hasY = False
	value = [ "", "", "", "", "" ]
	check = [ "", "", "", "", "" ]
	tempy = [ "", "", "", "", "" ]

	for i in range(5):
		if word[i] == solution[i]:
			value[i] = GREEN + word[i] + ENDC
			if hasY:
				if i in tempy:
					value[tempy.index(i)] = RED + word[tempy.index(i)] + ENDC
			check[i] = word[i]
			continue
		for j in range(5):
			if word[i] == solution[j] and word[i] != check[i] and word[j] != check[j] and tempy[j] != j:
				hasY = True
				value[i] = YELLOW + word[i] + ENDC
				tempy[i] = j
				break
			else:
				value[i] = RED + word[i] + ENDC
	for i in value:
		print(i,end="")
	print("")
	print("Try again.")

#MAIN
bank_file = open('wordle_list.txt')
bank = set(bank_file.read().split())
bank_file.close()
#bank = [ "beans", "house", "audio", "pears", "grape", "peony" ]
solution = random.choice(list(bank))
guesses = 6
print("Please enter first guess:")
while True:
	word = input()
	if word == solution:
		print("CORRECT! YOU WIN!")
		print(GREEN + word + ENDC)
		exit()
	if word not in bank:
		print("Not in word bank.")
		continue
	if len(word) == 5:
		guess(word, solution)
		guesses -= 1
		print(guesses,end="")
		print(" guesses left.")
	else:
		print("Hey, that's not 5 letters!")
	if guesses == 0:
		print("GAME OVER!")
		print("The word was: " + solution)
		exit()
		