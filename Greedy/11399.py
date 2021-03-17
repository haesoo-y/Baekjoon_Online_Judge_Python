def time_sum(list):
    time = 0
    for i in range(len(list)) :
        time += sum(list[:(i+1)])
    return time

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
answer = time_sum(lst)

print(answer)