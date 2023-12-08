def rev(word):
	pos = len(word)
	reverse = ""
	for i in range(len(word)):
		reverse += word[pos-1]
		pos -= 1
	print(reverse)

print("Please enter word to be reversed:")
word = raw_input()
print("Reversed word:")
rev(word)

