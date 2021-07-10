import sys
import heapq
input = sys.stdin.readline
# 보석 n개, 가방 k개, 무게 m, 가격 v, 최대무게 c
n, k = map(int, input().split())
pq = []
lst = []
bags = []
for _ in range(n):
    m, v = map(int, input().split())
    lst.append((m, v))
for _ in range(k):
    bags.append(int(input()))
bags.sort() # 오름차순으로 정렬
lst.sort(reverse=True) # 내림차순으로 정렬
answer = [0] * k
for i in range(k):
    while lst:
        if lst[-1][0] > bags[i]:
            break
        m, v = lst.pop()
        heapq.heappush(pq, (-v, m)) # 가격이 클 수록 먼저 pop
    if pq:
        v, m = heapq.heappop(pq)
        answer[i] = -v
print(sum(answer))