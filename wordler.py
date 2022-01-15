with open("dictionary.txt") as f:
	words = f.read().splitlines()
start_size = len(words)

#frequency percentage of each letter in the dictionary
freqs = {
"a":7.8,
"b":2,
"c":4,
"d":3.8,
"e":11,
"f":1.4,
"g":3,
"h":2.3,
"i":8.2,
"j":.21,
"k":2.5,
"l":5.3,
"m":2.7,
"n":7.2,
"o":6.1,
"p":2.8,
"q":.24,
"r":7.3,
"s":8.7,
"t":6.7,
"u":3.3,
"v":1,
"w":.91,
"x":.27,
"y":1.6,
"z":.44}

# score a word based on how frequent the letters are
# we want to use the most of the most common letters first
def score_word(word):
	return sum([freqs[e] for e in "".join(set(word))])

# important that a yellow clue is also NOT a green clue, hence the 2 conditions
def prune_yellow(words, letter, place):
	ans = []
	for e in words:
		if (letter in e) and (e[place] is not letter):
			ans.append(e)
	return ans

def prune_green(words, letter, place):
	ans = []
	for e in words:
		if e[place] == letter:
			ans.append(e)
	return ans

def prune_black(words, letter):
	ans = []
	for e in words:
		if letter not in e:
			ans.append(e)
	return ans

def prune(terms, word, colors):
	for ind in range(0, 5):
		letter = word[ind]
		code = colors[ind]
		#print(letter, code)
		if code == "b":
			ans = prune_black(terms, letter)
		elif code == "y":
			ans = prune_yellow(terms, letter, ind)
		elif code == "g":
			ans = prune_green(terms, letter, ind)
		terms = ans
	print("Prune reduced to", len(words), "possibilities")
	return terms

# could switch this out if I find the actual wordlist, which would eliminate the 0 error case
def main(words):
	t = 0
	while(True):
		t += 1
		bests = sorted(words, key=score_word)[::-1]
		filtered = len(bests)
		print("\nPossibilities filtered to", filtered, ". Next best move:\n=======\n", bests[0], "\n=======")
		print("Enter result as string OR 0 if word not allowed:")
		res = input()
		if res == "ggggg":
			print("Thanks for playing")
			return
		elif res == "0":
			words = bests[1:]
		else:
			words = prune(words, bests[0], res)

main(words)
