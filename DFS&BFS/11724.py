import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(n):
    for i in graph[n]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

global graph, visited
n, m = map(int ,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        dfs(i) # i와 연결된 노드 방문처리
        count += 1
print(count)