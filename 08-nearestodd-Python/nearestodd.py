# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	if(int(n)%2!=0):
		return int(n)
	if(round(n)%2!=0):
		return int(round(n))
	if(n%2==0):
		return int(n-1)
	if(((round(n)+1)-n)>0 and ((round(n)+1)-n)%2!=0):
		return int(round(n))+1
	else:
		return int(n)



