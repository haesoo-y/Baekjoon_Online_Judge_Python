import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    answer = lst[-1] - lst[-2]
    for i in range(n-2):
        answer = max(lst[i+2]-lst[i], answer)
    print(answer)