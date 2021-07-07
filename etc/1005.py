import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    q = deque()
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    dp = [0] * (n + 1)
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())
    # 위상정렬
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + time[i])
            if indegree[i] == 0 :
                q.append(i)
    print(dp[w])
