import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

invited = [1] + graph[1]
for i in graph[1] :
    for j in graph[i] :
        if j not in invited :
            invited.append(j)

print(len(invited) - 1)