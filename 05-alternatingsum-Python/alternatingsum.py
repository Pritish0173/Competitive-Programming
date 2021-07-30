# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.




def fun_alternatingsum(a): 
	if len(a) == 0:
		return 0
	flag = True
	Sum = 0
	for i in a:
		if flag:
			Sum += i
			flag = False
		else:
			Sum -= i
			flag = True
	return Sum


