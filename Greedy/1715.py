import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))
answer = 0
if n == 1:
    print(answer)
else:
    for _ in range(n-1):
        tmp_a = heapq.heappop(heap)
        tmp_b = heapq.heappop(heap)
        tmp = tmp_a + tmp_b
        answer += tmp
        heapq.heappush(heap,tmp)
    print(answer)