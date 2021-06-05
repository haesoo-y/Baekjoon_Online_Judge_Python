def find_parent(parent, n):
    if parent[n] != n :
        parent[n] = find_parent(parent, parent[n])
    return parent[n]

def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    for i in range(x+1, y+1):
        union_find(parent, x, i)

for i in range(1, n+1):
    find_parent(parent, i)

print(len(list(set(parent[1:]))))