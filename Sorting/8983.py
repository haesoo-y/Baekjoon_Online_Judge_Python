import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
m_lst = list(map(int, input().split()))
m_lst.sort()
n_lst = []
count = 0
for _ in range(n):
    a, b = map(int, input().split())
    n_lst.append((a, b))

for a, b in n_lst:
    start, end = 0, m
    while start <= end:
        mid = (start + end) // 2
        if mid == m:
            break
        dist = m_lst[mid] - a
        if abs(dist) + b <= l :
            count += 1
            break
        if dist == 0 :
            break
        elif dist < 0 :
            start = mid + 1
        else :
            end = mid - 1

print(count)
