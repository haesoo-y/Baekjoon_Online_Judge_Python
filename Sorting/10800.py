import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    c, s = map(int, input().split())
    lst.append((c, s, i))
lst.sort(key=lambda x:x[1])
size_sum = 0
color_sum = dict()
answer = []
start = 0

for end in range(n) :
    while lst[start][1] < lst[end][1]:
        size_sum += lst[start][1]
        color_sum[lst[start][0]] = color_sum.get(lst[start][0], 0) + lst[start][1]
        start += 1
    answer.append((lst[end][2], size_sum - color_sum.get(lst[end][0], 0)))

answer.sort()
for i in range(n):
    print(answer[i][1])
