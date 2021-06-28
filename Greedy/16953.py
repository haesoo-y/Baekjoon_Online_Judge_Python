a, b = map(int, input().split())
result = 1
while a < b :
    if b % 2 == 0:
        b = b//2
        result += 1
    else :
        if str(b)[-1] == '1' :
            b = int(str(b)[:-1])
            result += 1
        else :
            break

if a == b :
    print(result)
else :
    print(-1)