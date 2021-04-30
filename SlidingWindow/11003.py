import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
lst = list(map(int, input().split()))
dq = deque() # 가장 작은 값이 제일 왼쪽에 있도록
for i in range(n):
    while dq and dq[-1][1] > lst[i]:
        dq.pop()

    dq.append((i, lst[i]))

    if i >= l and dq[0][0] == i-l:
        dq.popleft()

    print(dq[0][1], end=' ')