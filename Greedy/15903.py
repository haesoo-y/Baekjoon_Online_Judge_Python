import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
heapq.heapify(lst)
for _ in range(m):
    x = heapq.heappop(lst)
    y = heapq.heappop(lst)
    nxy = x + y
    heapq.heappush(lst, nxy)
    heapq.heappush(lst, nxy)
print(sum(lst))