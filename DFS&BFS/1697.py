from collections import deque

def bfs(x, y):
    count = 0
    queue = deque()
    queue.append((x, count))
    visited = set()
    visited.add(x)
    while queue:
        new, count = queue.popleft()
        if new == y:
            return count
        for next in (new + 1, new - 1, new * 2):
            if 0 <= next < 100001 and next not in visited:
                queue.append((next, count+1))
                visited.add(next)

n, k = map(int, input().split())
print(bfs(n, k))