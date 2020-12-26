def Counting(n) :
    lst = [False, False] + [True]*(2*n-1)
    for i in range(2, 2*n+1):
        if lst[i] :
            for j in range(i+i, 2*n+1, i):
                lst[j] = False
    return lst[n+1:2*n+1]

while True :
    x = int(input())
    if x == 0 :
        break
    print(Counting(x).count(True))

