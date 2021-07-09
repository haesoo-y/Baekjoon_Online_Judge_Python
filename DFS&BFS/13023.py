import sys
input = sys.stdin.readline

def dfs(num, depth):
    if depth >= 4 :
        return 4
    for new in graph[num]:
        if visited[new] :
            continue
        visited[new] = True
        tmp = dfs(new, depth + 1)
        visited[new] = False
        if tmp and tmp >= 4:
            return 4

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
global visited
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    visited = [False] * n
    d = 0
    if not graph[i] :
        continue
    visited[i] = True
    d = dfs(i, d)
    if d :
        print(1)
        quit()
print(0)