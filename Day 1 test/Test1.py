def generate_series(n):
    s = ""
    for i in range(n):
        j = 0
        while j <= i:
            s += str(j+1) + " "
            j += 1
        s = s[:-1]
        s += "\n"

    return s

print(generate_series(5))
