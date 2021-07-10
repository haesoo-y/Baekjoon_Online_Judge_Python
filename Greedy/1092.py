import sys
input = sys.stdin.readline

n = int(input())
c_lst = list(map(int, input().split())) # 크레인 무게 제한 리스트
c_lst.sort(reverse=True)
answer = [0] * n
m = int(input())
b_lst = list(map(int, input().split())) # 박스 무게 리스트
b_lst.sort(reverse=True)
if b_lst[0] > c_lst[0]:
    print(-1)
    quit()
time = (m-1) // n + 1
box = 0
while box < m:
    for i in range(n):
        if answer[i] < time and c_lst[i] >= b_lst[box]:
            answer[i] += 1
            box += 1
            break
        if c_lst[i] < b_lst[box]:
            time += 1
            break

print(max(answer))
