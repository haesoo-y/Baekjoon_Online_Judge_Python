n = int(input())
dp = [0 for _ in range(31)]
lst = [2 for _ in range(31)]
lst[2] = 3
dp[0] = 1
for i in range(2, n+1, 2):
    for j in range(0,i,2):
        dp[i] += dp[j] * lst[abs(i-j)]
print(dp[n])