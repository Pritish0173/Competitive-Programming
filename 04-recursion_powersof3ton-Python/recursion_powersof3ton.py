# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def powersOf3ToN(n,num,l):
	if num==1:
		return [1]
	if (3**n)<=num:
		return l + [3**n] + powersOf3ToN(n+1,num,l)
	return l
	

def recursion_powersof3ton(n):
	# Your code goes here
	if n<1:
		return None
	l = []
	return powersOf3ToN(0,n,l)