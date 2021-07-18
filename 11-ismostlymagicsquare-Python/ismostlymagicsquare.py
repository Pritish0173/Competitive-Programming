# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def horizontal(a):
	Sum = set()
	s = 0
	for i in range(len(a)):
		h = sum(a[i])
		Sum.add(h)
		s = h
	if(len(Sum)>1):
		return False
	return s

def vertical(a):
	Sum = set()
	s = 0
	for i in range(len(a)):
		l = [a[x][i] for x in range(len(a))]
		v = sum(l)
		Sum.add(v)
		s = v
	if(len(Sum)>1):
		return False
	return s

def diagonal(a):
	d1 = 0
	d2 = 0
	for i in range(len(a)):
		d1 += a[i][i]
		d2 += a[-i-1][-i-1]
	if(d1!=d2):
		return False
	return d1	

def ismostlymagicsquare(a):
	# Your code goes here
	hor = horizontal(a)
	ver = vertical(a)
	diag = diagonal(a)
	if(hor and ver and diag):
		if(hor==ver and ver==diag and diag==hor):
			return True
	return False

	