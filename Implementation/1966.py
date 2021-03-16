case = int(input())
for _ in range(case):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    count = 0
    while lst[m] != 0 :
        for i in range(n):
            if lst[i] == max(lst):
                lst[i] = 0
                count += 1
                if i == m :
                    break
    print(count)
