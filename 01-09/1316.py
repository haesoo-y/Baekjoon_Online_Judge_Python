def groupcount(x,c) :
    while x != '':
        if x[1:].find(x[0]) < 1:
            x = x[1:]
        else:
            c += 0
            break
    else:
        c += 1
    return c

N = int(input())
i = 0
for _ in range(N) :
    s = input()
    i = groupcount(s,i)
print(i)


