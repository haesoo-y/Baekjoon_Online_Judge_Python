from collections import deque

def bfs(g):
    queue = deque()
    queue.append((0,0))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            move_x = x + dx[i]
            move_y = y + dy[i]
            if move_x < 0 or move_x >= n or move_y < 0 or move_y >= m:
                continue
            if g[move_x][move_y] == 1:
                queue.append((move_x, move_y))
                g[move_x][move_y] = g[x][y] + 1

n, m =map(int, input().split())
graph = list()
for _ in range(n):
    graph.append(list(map(int, input())))

bfs(graph)
print(graph[n-1][m-1])