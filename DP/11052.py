import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp = [i for i in lst]
if n == 1 :
    print(dp[0])
    quit()
for i in range(1, n):
    for j in range(i//2 + 1):
        dp[i] = max(dp[j]+dp[i-1-j], dp[i])
print(dp[-1])
