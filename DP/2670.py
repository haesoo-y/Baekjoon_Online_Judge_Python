import sys
input = sys.stdin.readline

n = int(input())
dp = []
for _ in range(n):
    dp.append(float(input()))

for i in range(1, n):
    dp[i] = max(dp[i], dp[i]*dp[i-1])

print('%.3f'%(max(dp)))