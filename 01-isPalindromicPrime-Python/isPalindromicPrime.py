# Write a function isPalindromicPrime that takes a value n as a parameter and returns True if the given n is a palindrome and prime and False otherwise.

def isPrime(n):
	if(n<2):
		return False
	if(n == 2):
		return True
	if(n%2==0):
		return False
	maxfactor = round(n**0.5)
	for i in range(3,maxfactor+1,2):
		if(n%i==0):
			return False
	return True

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def IsPalindromicPrime(n):
    if isPalindrome(n) and isPrime(n):
        return True
    else:
        return False

# Test Cases
assert (IsPalindromicPrime(2) == True)
assert (IsPalindromicPrime(10) == False)
assert (IsPalindromicPrime(104) == False)
assert (IsPalindromicPrime(235) == False)
assert (IsPalindromicPrime(131) == True)
assert (IsPalindromicPrime(900) == False)
assert (IsPalindromicPrime(101) == True)
assert (IsPalindromicPrime(383) == True)
assert (IsPalindromicPrime(373) == True)
assert (IsPalindromicPrime(121) == False)
print("All test cases passed... :-)")