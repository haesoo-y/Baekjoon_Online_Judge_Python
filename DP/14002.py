import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)
index = dp.index(max(dp))
count = max(dp)
answer = []
print(count)
for i in range(index,-1,-1):
    if dp[i] == count :
        answer.append(lst[i])
        count-=1
answer.reverse()
for i in answer:
    print(i, end=' ')