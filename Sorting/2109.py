import sys
import heapq
input = sys.stdin.readline

answer = []
n = int(input())
lst = []
for _ in range(n):
    p, d = map(int, input().split())
    lst.append((p,d))

lst.sort(key=lambda x:(x[1],-x[0]))
d = 1
for i in range(n):
    if lst[i][1] >= d:
        d += 1
        heapq.heappush(answer, lst[i][0])
    else :
        if lst[i][0] > answer[0] :
            heapq.heappop(answer)
            heapq.heappush(answer, lst[i][0])

print(sum(answer))