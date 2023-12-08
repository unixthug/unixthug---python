#wordle by Adam Jones for Python | 12/8/2023

import random

#COLORS
GREEN = '\033[42m'
RED = '\033[41m'
YELLOW = '\033[43m'
ENDC = '\033[0m'

#GUESS FUNCTION
def guess(word, solution):
	value = [ "", "", "", "", "" ]
	temp = 0
	if word == solution:
		print("CORRECT! YOU WIN!")
		print(GREEN + word + ENDC)
		exit()
	for i in range(len(word)):
		for j in range(len(solution)):
			if word[i] == solution[j] or word[i] != value[i]:
				if word[i] == solution[i]:
					value[i] = GREEN + word[i] + ENDC
				elif word[i] == solution[j] and temp != j:
					value[i] = YELLOW + word[i] + ENDC
					temp = j
				else:
					value[i] = RED + word[i] + ENDC

	for i in value:
		print(i, end="")
	print("")
	print("Try again.")

#MAIN
bank = [ "beans", "house", "audio", "pears", "grape", "peony", "apple" ]
solution = random.choice(bank)
guesses = 6
print("Please enter first guess:")
while True:
	guess(input(), solution)
	guesses -= 1
	print(guesses, end="")
	print(" guesses left.")
	if guesses == 0:
		print("GAME OVER!")
		exit()
