k = int(input())
lst = []
for _ in range(k):
    num = int(input())
    if num > 0 :
        lst.append(num)
    else :
        if len(lst) == 0 :
            continue
        lst.pop()

print(sum(lst))