import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def find_parent(parent, k):
    if k != parent[k]:
        parent[k] = find_parent(parent, parent[k])
    return parent[k]

def union_find(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y :
        parent[y] = x
    else :
        parent[x] = y

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    z, a, b = map(int, input().split())
    if z == 0 :
        union_find(parent, a, b)
    else :
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else :
            print('NO')