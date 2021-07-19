# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def ispalindrome(n):
	s = str(n)
	p = s[::-1]
	if(s == p):
		return True
	else:
		return False

def numberreverse(n):
	s = str(n)
	p = s[::-1]
	return int(p)

def islychrel(n):
	for _ in range(30):
		n += numberreverse(n)
		if(ispalindrome(n)):
			return False
	return True

def nthlychrelnumbers(n):
	# your code goes here
	found = 0
	guess = 0
	while found < n:
		guess += 1
		if(islychrel(guess)):
			found += 1
	return guess