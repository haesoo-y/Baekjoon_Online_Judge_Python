import sys
from collections import deque
input = sys.stdin.readline

def dfs(x, g):
    print(x, end=' ')
    visited[x] = True
    for i in g[x]:
        if visited[i] == False :
            dfs(i, g)

def bfs(x, g):
    print(x, end=' ')
    visited[x] = True
    queue = deque()
    queue.append(x)
    while queue :
        nx = queue.popleft()
        for i in g[nx]:
            if visited[i] == False :
                queue.append(i)
                visited[i] = True
                print(i, end=' ')



n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, num = map(int, input().split())
    graph[i].append(num)
    graph[num].append(i)
for i in range(len(graph)):
    graph[i].sort()

global visited
visited = [False] * (n + 1)
dfs(v, graph)
print()

visited = [False] * (n + 1)
bfs(v, graph)
