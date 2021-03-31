import sys
input = sys.stdin.readline

def dfs(number, index):
    visited[number] = True
    if not visited[graph[number]] :
        dfs(graph[number], index)
    elif visited[graph[number]] and graph[number] == index:
        answer.append(index)

n = int(input())
graph = [0]
answer = []

for i in range(n):
    graph.append(int(input()))

for i in range(1, n+1):
    visited = [False] * (n + 1)
    dfs(i, i)

answer.sort()
print(len(answer))
for i in answer :
    print(i)