import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    w = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                w += 1
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return w

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

cnt = 0
big = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 0
            cnt += 1
            tmp = bfs(i, j)
            big = max(big, tmp)
print(cnt)
print(big)