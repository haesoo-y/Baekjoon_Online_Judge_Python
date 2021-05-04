import sys

def time_stamp(x, y):
    result = 0
    day_lst = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(12):
        if i == x:
            break
        result += day_lst[i]

    return result + y

input = sys.stdin.readline
n = int(input())
day_lst = []
for _ in range(n):
    a,b,c,d = map(int, input().split())
    day_lst.append((time_stamp(a,b), time_stamp(c,d)))
# 3월 1일 : 60 , 11월 30일 : 334
day_lst.sort()
index = 0
answer = [(60,60)]
while answer[-1][1] <= 334:
    tmp = (0, 0)
    start = index
    for i in range(start, n):
        if day_lst[i][0] <= answer[-1][1]:
            if day_lst[i][1] > tmp[1]:
                tmp = day_lst[i]
                index = i+1
    if tmp[1] == 0 :
        answer = [0]
        break
    else :
        answer.append(tmp)

print(len(answer) - 1)
