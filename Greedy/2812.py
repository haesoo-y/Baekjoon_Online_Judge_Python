import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().strip()))
count = 0
result = []
for i in range(n):
    while count < k and result :
        if result[-1] < lst[i]:
            result.pop()
            count += 1
        else:
            break
    result.append(lst[i])

for i in range(n-k):
    print(result[i], end='')
