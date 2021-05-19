import sys
input = sys.stdin.readline

n, l = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
tmp = lst[0]
count = 1
if n == 1:
    print(count)
    quit()
for i in range(1, n):
    if lst[i] >= tmp + l:
        tmp = lst[i]
        count += 1
print(count)