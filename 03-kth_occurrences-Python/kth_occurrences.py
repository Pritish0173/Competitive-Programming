# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
    setstr = set(s)
    d = {}
    for i in setstr:
        d[i] = s.count(i)
    l = []
    for i in d:
        l.append([d[i],i])
    l.sort()
    l = l[::-1]
    return l[n-1][1]


