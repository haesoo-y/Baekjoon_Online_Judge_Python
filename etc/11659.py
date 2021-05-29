import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
accum_lst = [0] * (n+1)
for i in range(0, n):
    accum_lst[i + 1] = accum_lst[i] + lst[i]

for _ in range(m):
    x, y = map(int, input().split())
    print(accum_lst[y] - accum_lst[x-1])