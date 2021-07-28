# Recursion-Only recursion_secondlargest(L) [15 pts]
# Note: recall that you may not use sort, sorted, min, or max this week! With that in mind, write the function 
# recursion_secondlargest(L) that takes a list of integers in any order and returns the second-largest value in the list. To 
# be more precise, it returns the second value from the end if the list was sorted (though you do not need to sort 
# it to solve this problem), so if the largest value occurs twice, you would return that value. Also, if there are 
# fewer than 2 values in the list, return None. Here are some test cases:
# assert(recursion_secondlargest([1,2,3,4,5]) == 4)
# assert(recursion_secondlargest([4,3]) == 3)
# assert(recursion_secondlargest([4,4,3]) == 4)
# assert(recursion_secondlargest([-3,-4]) == -4)
# assert(recursion_secondlargest([4]) == None)
# assert(recursion_secondlargest([ ]) == None)
# Again, you do not need to sort the list. We didn't sort it in our sample solution. We just tracked the two largest 
# values as we recursively traversed the list. Also, you may not use loops/iteration in this problem

def secondlargest(L,i,Prev,Next,count):
    if i==0:
        if L[i]>L[i+1]:
            Prev = L[i+1]
            Next = L[i]
            count += 1
        else:
            Prev = L[i]
            Next = L[i+1]
            count += 1
        return secondlargest(L,i+2,Prev,Next,count)
    if i==len(L):
        if count==1:
            return Prev
        else:
            return Next
    if L[i]>Next:
        if L[i]>Prev:
            Prev = Next
        Next = L[i]
        count = 1
    else:
        if L[i]==Next:
            count += 1
        if L[i]<Next and L[i]>Prev:
            Prev = L[i]
    return secondlargest(L,i+1,Prev,Next,count)


def recursion_secondlargest(L):
	# Your code goes here
    if len(L)<2:
        return None
    if len(L)==2:
        if L[0]>L[1]:
            return L[1]
        else:
            return L[0]
    return secondlargest(L,0,0,0,0)