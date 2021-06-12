import sys
input = sys.stdin.readline

def find_parent(parent, n):
    if parent[n] != n:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y :
        parent[y] = x
    else :
        parent[x] = y

v, e = map(int, input().split())
parent = [i for i in range(v+1)]
edges = []
result = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
# Kruskal
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
print(result)