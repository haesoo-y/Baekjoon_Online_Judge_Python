lst = list([0]*100 for i in range(100))
# for i in range(100) :
#     print(lst[i])
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            lst[j][k] = 1

answer = 0
for i in range(len(lst)):
    answer += sum(lst[i])

print(answer)