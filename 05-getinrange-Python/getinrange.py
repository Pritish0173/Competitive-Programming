# Write the function getInRange(x, bound1, bound2) which takes 3 int values
# x, bound1, and bound2, where bound1 is not necessarily less than bound2. 
# If x is between the two bounds, just return it unmodified. Otherwise, 
# if x is less than the lower bound, return the lower bound, 
# or if x is greater than the upper bound, return the upper bound.

def fun_getinrange(x, bound1, bound2):
	# your code goes here
	upperbound = 0
	lowerbound = 0
	if(bound1 < bound2):
		lowerbound = bound1
		upperbound = bound2
	if(bound1 > bound2):
		lowerbound = bound2
		upperbound = bound1
	if(lowerbound<x<upperbound):
		return x
	if(x<lowerbound):
		return lowerbound
	if(x>upperbound):
		return upperbound
