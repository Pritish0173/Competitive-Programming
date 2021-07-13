def generate_series(n):
    s = ""
    flag = True
    for i in range(n):
        j = 0
        while j <= i:
            if(flag):
               s += "1 "
            else:
                s += "0 "
            flag = not flag
            j += 1
        s = s[:-1] + "\n"
    return s

print(generate_series(5))