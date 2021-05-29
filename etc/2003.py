import sys
input = sys.stdin.readline
n, m = map(int, input().split())
count = 0
lst = list(map(int, input().split()))
start, end = 0, 0
interval_sum = lst[0]
while start < n and end < n:
    if interval_sum == m:
        count += 1

    if interval_sum <= m:
        end += 1
        if end == n:
            break
        interval_sum += lst[end]
    else :
        interval_sum -= lst[start]
        start += 1

print(count)
