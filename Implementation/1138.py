n = int(input())
big_left = list(map(int, input().split()))
answer_lst = [0] * n

for i in range(n):
    big = big_left[i]
    num = i + 1
    count = 0
    for j in range(n):
        if big == count and answer_lst[j] == 0 :
            answer_lst[j] = num
            break
        if answer_lst[j] == 0:
            count += 1

for i in answer_lst :
    print(i, end=' ')