import sys
input = sys.stdin.readline

x = '0' + input().strip()
y = '0' + input().strip()
x_len = len(x)
y_len = len(y)

dp = [[0]*(y_len) for _ in range(x_len)]

for i in range(1, x_len):
    for j in range(1, y_len):
        if x[i] == y[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])