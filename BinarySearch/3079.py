import sys
input = sys.stdin.readline

n, m = map(int, input().split())
time = []
answer = 0
for _ in range(n):
    time.append(int(input()))
time.sort()
start = 0
end = time[-1] * m
while start <= end :
    mid = (start + end) // 2 # 목표 최종 시간
    people = 0 # mid 시간 내에서 달성가능한 인원
    for t in time :
        if t > mid :
            break
        people += mid // t # 각 심사대에서 확인가능한 인원 수 더하기
    if people >= m:
        answer = mid
        end = mid - 1
    else :
        start = mid + 1
print(answer)
