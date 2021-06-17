import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
lst = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    lst.append((w, v))

for i in range(1, n+1):
    nw, nv = lst[i][0], lst[i][1]
    for j in range(1, k+1):
        if j >= nw :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-nw] + nv)
        else :
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])