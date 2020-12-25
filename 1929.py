M, N = map(int, input().split())
x = [False, False]+[True]*(N-1)
for i in range(2, N+1):
    if x[i] :
        if i >= M:
            print(i)
        for j in range(i+i,N+1,i) :
            x[j] = False
