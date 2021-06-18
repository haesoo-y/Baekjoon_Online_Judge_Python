n = int(input())
if n == 1 :
    print(1)
    quit()
dp = [1] * (n+1)
dp[2] = 3
for i in range(2, n+1):
    dp[i] = dp[i-1] + (dp[i-2]*2)
print(dp[n]%10007)