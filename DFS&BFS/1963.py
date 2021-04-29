import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append((x, 0))
    visited = [False] * 10000

    while queue :
        num, count = queue.popleft()
        if num == y:
            return count
        for i in range(4):
            for n in range(10):
                new_num = int(str(num)[:i] + str(n) + str(num)[i+1:])
                if visited[new_num] :
                    continue
                if new_num < 1000 :
                    continue
                if e_lst[new_num]:
                    visited[new_num] = True
                    queue.append((new_num, count + 1))
    return "Impossible"


e_lst = [True] * 10000
for i in range(2, 101):
    if e_lst[i]:
        c = 2
        while i*c < 10000:
            e_lst[i*c] = False
            c += 1

for t in range(int(input())):
    a, b = map(int , input().split())
    result = bfs(a, b)
    print(result)