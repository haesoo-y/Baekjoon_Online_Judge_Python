lst = list()
for _ in range(9) :
    lst.append(int(input()))
max_n = lst[0]
max_i = 0
for i in range(1, 9) :
    if max_n < lst[i] :
        max_n = lst[i]
        max_i = i+1
print(max_n)
print(max_i)