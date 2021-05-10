import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(num):
    global answer
    if graph[num]:
        left, right = 0,0
        for i, d in graph[num]:
            now_distance = dfs(i) + d
            if now_distance > right:
                left, right = right, now_distance
            elif now_distance > left:
                left = now_distance
        answer = max(answer, left+right)
        return right
    else:
        return 0

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y, c = map(int, input().split())
    graph[x].append((y,c))

answer = 0
dfs(1)
print(answer)