import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
dp = [0] * n
dp[0] = lst[0]
for i in range(n):
    if i <= 1:
        dp[i] = sum(lst[:i+1])
    elif i == 2:
        dp[i] = max(dp[i-2] + lst[i], lst[i-1] + lst[i], dp[i - 1])
    else :
        dp[i] = max(dp[i-3] + lst[i] + lst[i - 1], dp[i-2] + lst[i], dp[i-1])
print(dp[-1])

