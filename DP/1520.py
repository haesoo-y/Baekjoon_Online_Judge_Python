import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    if x == m - 1 and y == n - 1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[x][y] > graph[nx][ny] :
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

global m, n, dp
m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))
dp = [[-1] * n for _ in range(m)]
answer = dfs(0,0)
print(answer)