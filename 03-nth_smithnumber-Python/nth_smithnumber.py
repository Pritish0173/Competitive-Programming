# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def digitsum(n):
    Sum = 0
    s = str(n)
    for i in s:
        Sum += int(i)
    return Sum

def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    maxfactor = round(n**0.5)
    for i in range(3,maxfactor+1,2):
        if n%i==0:
            return False
    return True

def isComposite(n):
    if not isPrime(n):
        return True
    return False

def primefactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def isSmithNumber(n):
    if not isComposite(n):
        return False
    pfl = primefactors(n)
    l = [digitsum(i) for i in pfl]
    Sum = sum(l)
    numsum = digitsum(n)
    if Sum==numsum:
        return True
    return False

def fun_nth_smithnumber(n):
    found = -1
    guess = 0
    while found<n:
        guess += 1
        if isSmithNumber(guess):
            found += 1
    return guess