N = int(input())
lst = list(map(int, input().split()))
count = 0
for i in lst :
    if i == 1 :
        continue
    elif i == 2 :
        count += 1
    else :
        for j in range(2,i) :
            if i % j == 0 :
                break
            elif j == i-1 :
                count += 1
print(count)

