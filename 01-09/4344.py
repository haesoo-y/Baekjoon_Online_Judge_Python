N = int(input())
for _ in range(N) :
    case = list(map(int, input().split()))
    # print(case)
    n = case[0]
    lst = case[1:]
    avg = sum(lst)/n
    # print(lst)
    count = 0
    for i in range(n):
        if lst[i] > avg :
            count += 1
    rnd = round(count/n*100,3)
    print('%.3f%%' %rnd)
    # print('%.3f' %round)




