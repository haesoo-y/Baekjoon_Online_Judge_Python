import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input().strip())
    lst.sort()
    answer = 'YES'
    for x in range(1, len(lst)):
        if lst[x].find(lst[x-1]) == 0:
            answer = 'NO'
            break
    print(answer)