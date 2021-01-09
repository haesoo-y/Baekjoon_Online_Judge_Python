N, M = map(int, input().split())
lst = list(map(int,input().split()))

answer = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if lst[i]+lst[j]+lst[k] > answer and lst[i]+lst[j]+lst[k] <= M :
                answer = lst[i]+lst[j]+lst[k]

print(answer)

#
# 10 500
# 93 181 245 214 315 36 185 138 216 295
# 497

# 5 21
# 5 6 7 8 9