import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
dp = [0 for i in range(k + 1)]
dp[0] = 1
for i in range(n):
    lst.append(int(input()))
for i in lst:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[k])