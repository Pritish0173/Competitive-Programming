# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def sumOfSquaresOfDigits(n):
    s = str(n)
    Sum = 0
    for i in s:
        Sum += int(i)**2
    return Sum
    

def ishappyprimenumber(n):
    # Your code goes here
    for i in range(30):
        Sum = sumOfSquaresOfDigits(n)
        print(Sum)
        if Sum==1:
            return True
        if Sum==4:
            return False
        n = Sum
    # return False
