import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    start, end = map(int,input().split())
    lst.append((start, end))
lst.sort(key=lambda x:(x[0],x[1]))
# print(lst)
answer = []
answer.append(lst[0])
for i in range(1, n):
    if lst[i][0] >= answer[-1][1]:
        answer.append(lst[i])
    elif lst[i][1] < answer[-1][1] :
        answer[-1] = lst[i]
print(len(answer))