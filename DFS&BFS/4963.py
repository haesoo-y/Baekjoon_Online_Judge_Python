from collections import deque

def bfs(x, y) :
    queue = deque()
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for i in range(8) :
            move_x = x + dx[i]
            move_y = y + dy[i]
            if move_x < 0 or move_y < 0 or move_x >= h or move_y >= w :
                continue
            if graph[move_x][move_y] == 1 :
                graph[move_x][move_y] = 0
                queue.append((move_x, move_y))

while True :
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break
    graph = list()
    count = 0
    for i in range(h):
        graph.append(list(map(int, input().split())))

    # print(graph)
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 :
                graph[i][j] = 0
                count += 1
                bfs(i, j)

    print(count)