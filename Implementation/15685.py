import sys
input = sys.stdin.readline

def get_graph(x, y, d, g):
    dx = [1, 0, -1, 0]
    dy = [0 ,-1, 0, 1]
    graph[x][y] = 1
    lst = [d]
    tmp = [d]
    for i in range(g + 1):
        for j in lst:
            x += dx[j]
            y += dy[j]
            graph[x][y] = 1
        lst = [(k + 1) % 4 for k in tmp]
        lst.reverse()
        tmp = tmp + lst

n = int(input())
graph = [ [0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    get_graph(x, y, d, g)

result = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] + graph[i][j+1] + graph[i+1][j] + graph[i+1][j+1] == 4:
            result += 1

print(result)