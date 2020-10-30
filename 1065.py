N = int(input())
if N < 100 :
    count = N
elif N < 1000 :
    count = 99
    for i in range(100,N+1) :
        hh = i // 100
        tt = (i % 100) // 10
        dd = (i % 100) % 10
        if hh-tt == tt-dd :
            count += 1
        else :
            pass
elif N == 1000 :
    count = 99
    for i in range(100,N) :
        hh = i // 100
        tt = (i % 100) // 10
        dd = (i % 100) % 10
        if hh-tt == tt-dd :
            count += 1
        else :
            pass


print(count)

