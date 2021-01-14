prime = [0,0] + [i for i in range(2,10001)]
for i in range(2,10001) :
    if prime[i] :
        for j in range(i+i, 10001, i):
            prime[j] = 0

# print(prime[0:20])
# [0, 0, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19]

T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(n//2,0,-1):
        if prime[i] :
            if prime[n-i]:
                print(i, n-i)
                break