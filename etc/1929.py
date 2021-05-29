import sys
input = sys.stdin.readline

m, n = map(int, input().split())

prime_bool = [True] * (n + 1)
prime_bool[0] = False
prime_bool[1] = False
for i in range(2, int(n**0.5) + 1):
    if prime_bool[i] :
        j = 2
        while i * j <= n :
            prime_bool[i * j] = False
            j += 1

for i in range(m, n+1):
    if prime_bool[i]:
        print(i)