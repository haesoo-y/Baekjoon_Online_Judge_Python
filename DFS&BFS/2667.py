import sys
input = sys.stdin.readline

def dfs(x, y, c):
    graph[x][y] = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or mx >= n or my < 0 or my >= n:
            continue
        elif graph[mx][my] == 1:
            c.append(1)
            dfs(mx, my, c)
    return c

n = int(input())
graph = [''] * n

for i in range(n):
    graph[i] = (list(map(int, input().strip())))

count = 0
lst = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 :
            answer = [1]
            count += 1
            answer = dfs(i, j, answer)
            lst.append(len(answer))

print(count)
lst.sort()
for i in lst :
    print(i)