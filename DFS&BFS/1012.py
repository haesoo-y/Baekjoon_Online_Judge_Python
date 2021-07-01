from collections import deque
import sys
input = sys.stdin.readline

def bfs(y, x):
    graph[y][x] = 0
    queue = deque()
    queue.append((y, x))
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m :
                continue
            if graph[ny][nx] == 1 :
                graph[ny][nx] = 0
                queue.append((ny, nx))

t = int(input())
global graph
for _ in range(t):
    count = 0
    m, n, k = map(int, input().split()) # 가로 m, 세로 n
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split()) # 가로위치 x, 세로위치 y
        graph[y][x] = 1
    # 그래프 탐색
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count += 1
                bfs(i, j)
    print(count)