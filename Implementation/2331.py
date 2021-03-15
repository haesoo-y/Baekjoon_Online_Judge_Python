def multiply_p(x) :
    x = int(x) ** p
    return x

a, p = map(int, input().split())
lst = [a]
i = 0
# lst.append(0)
# lst[1] = sum(map(multiply_p, str(lst[0])))
while True :
    i += 1
    num = sum(map(multiply_p, str(lst[i-1])))
    if num in lst :
        break
    lst.append(num)

print(lst.index(num))