M = int(input())
N = int(input())
lst = list()
for i in range(M,N+1) :
    if i == 1 :
        continue
    elif i == 2:
        lst.append(2)
        continue
    else :
        for j in range(2,i) :
            if i % j == 0 :
                break
            elif j == i-1:
                lst.append(i)
if lst :
    print(sum(lst))
    print(min(lst))
else :
    print(-1)
