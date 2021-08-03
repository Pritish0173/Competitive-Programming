# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

def permutations(x):
	if len(x) == 0:
		return []
	if len(x) == 1:
		return [x]
	l = []
	for i in range(len(x)):
		m = x[i]
		rem = x[:i] + x[i+1:]
		for p in permutations(rem):
			l.append([m] + p)
	return l

def getallpermutations(x):
	# Your code goes here
	l = permutations(list(x))
	l = list(map(tuple, l))
	return l