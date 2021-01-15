N = int(input())
lst = []
for i in range(N) :
    w,h = map(int,input().split())
    lst.append((w,h))
# print(lst)
# [(55, 185), (58, 183), (88, 186), (68, 175), (46, 155)]
# print(lst[1][1])
# 183
for i in range(N) :
    rank = 1
    for j in range(N) :
        # i는 리스트안의 순서를 차례로 반환
        # j는 비교대상들을 차례로 반환
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1] :
            rank += 1
    print(rank,end=" ")