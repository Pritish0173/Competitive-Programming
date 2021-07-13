# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
    a = abs(n)
    l = list(str(a))
    l = l[::-1]
    print(l)
    if(k>=len(l)):
        l.append(str(d))
    else: 
        for i in range(len(l)):
            if(i==k):
                l[i] = str(d)
    l = l[::-1]
    print(l)
    a = int("".join(l))
    n = int(a*(int(n/abs(n))))
    return n

