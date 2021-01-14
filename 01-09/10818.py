n = int(input())
lst = input().split()
max = int(lst[0])
min = int(lst[0])
for i in range(1,n) :
    if int(lst[i]) > max :
        max = int(lst[i])
    if int(lst[i]) < min :
        min = int(lst[i])
print(min, max)


