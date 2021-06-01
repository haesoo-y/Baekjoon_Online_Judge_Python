import sys
input = sys.stdin.readline

n = int(input())
dp = [[1]*10 for _ in range(n+1)]
for i in range(1, n+1):
    if i == 1 :
        continue
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])

print(sum(dp[n])%10007)
