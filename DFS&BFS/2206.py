from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, z):
    visited[x][y][z] = 1
    queue = deque()
    queue.append((x, y, z)) # x, y, z
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue :
        x, y, z = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny][z]:
                continue
            if graph[nx][ny] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
            if graph[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][z] + 1
                queue.append((nx, ny, 1))

n, m = map(int, input().split())
global graph, visited
graph = []
# visited[x][y][z] z가 0인곳에 벽을 뚫지 않았을 때의 방문처리 1인곳에 벽을 뚫었을 때의 방문처리
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().strip())))
bfs(0,0,0)
answer = visited[n-1][m-1]
if answer[0] == 0 and answer[1] == 0 : # 둘 다 0이면 -1 출력
    print(-1)
elif answer[0] > 0 and answer[1] > 0 : # 둘 다 0이 아니면 작은 값 출력
    print(min(answer))
else : # 둘 중하나가 0이면 0이 아닌 값 출력
    print(max(answer))