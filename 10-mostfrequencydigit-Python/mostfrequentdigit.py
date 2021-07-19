# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	a = abs(n)
	s = str(a)
	ss = set(s)
	d = {}
	for i in ss:
		d[i] = s.count(i)
	maximum = max(d.values())
	l = [int(i) for i in d if d[i]==maximum]
	return min(l)
