import sys
from collections import deque
input = sys.stdin.readline

def bfs(queue):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m  :
                continue
            if graph[nx][ny] == -1 :
                continue
            else :
                if graph[nx][ny] == 0:
                    graph[nx][ny] = d + 1
                    queue.append((nx, ny, d + 1))

global m, n, graph, day
m, n = map(int, input().split())
graph = []
queue = deque()
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j, 1))
bfs(queue)

# print(graph)
# [[9, 8, 7, 6, 5, 4], [8, 7, 6, 5, 4, 3], [7, 6, 5, 4, 3, 2], [6, 5, 4, 3, 2, 1]]
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            quit()
        answer = max(answer, graph[i][j])

print(answer-1)