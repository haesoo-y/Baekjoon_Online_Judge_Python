import sys
input = sys.stdin.readline

def find_parent(parents, num):
    if parents[num] != num:
        parents[num] = find_parent(parents, parents[num])
    return parents[num]

def union_parent(parents, x, y):
    x = find_parent(parents, x)
    y = find_parent(parents, y)
    if x < y:
        parents[y] = x
    else :
        parents[x] = y

n = int(input())
m = int(input())
result = 0
graph = []
parents = [i for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

for tp in graph:
    c, a, b = tp
    if find_parent(parents, a) != find_parent(parents, b):
        result += c
        union_parent(parents, a, b)
print(result)