# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 

def factorial(n):
	if(n==1 or n==0):
		return 1
	return n*factorial(n-1)

def combination(n,r):
	c = factorial(n)/(factorial(r)*factorial(n-r))
	return int(c)

def fun_pascaltrianglevalue(row, col):
    if(col>row):
        return 0
    if(col==0 or row==0):
        return 1
    n = row
    r = col
    value = combination(n,r)
    return value