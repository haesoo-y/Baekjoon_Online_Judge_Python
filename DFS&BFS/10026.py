import sys
import copy
from collections import deque

def color_change(graph):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'R':
                graph[i][j] = 'G'

def bfs(graph, x, y):
    color = graph[x][y]
    graph[x][y] = 'O'
    queue = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue.append((x, y))
    while queue :
        nx, ny = queue.popleft()
        for i in range(4):
            move_x = nx + dx[i]
            move_y = ny + dy[i]
            if move_x < 0 or move_x >= n or move_y < 0 or move_y >= n :
                continue
            if graph[move_x][move_y] == color:
                graph[move_x][move_y] = 'O'
                queue.append((move_x, move_y))

input = sys.stdin.readline

graph_n = []
graph_u = []
n = int(input().strip())
for _ in range(n):
    graph_n.append(list(map(str, input().strip())))

graph_u = copy.deepcopy(graph_n)
color_change(graph_u)
answer_n, answer_u = 0, 0

for i in range(n):
    for j in range(n):
        if graph_n[i][j] != 'O':
            answer_n += 1
            bfs(graph_n, i, j)
        if graph_u[i][j] != 'O':
            answer_u += 1
            bfs(graph_u, i, j)

print(answer_n, answer_u)