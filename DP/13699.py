import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 36
dp[0], dp[1] = 1, 1

for i in range(2,n+1):
    for j in range(i):
        x, y = dp[j], dp[i-1-j]
        dp[i] += x * y

print(dp[n])