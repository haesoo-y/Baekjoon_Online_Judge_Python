n, m = map(int, input().split())
if n >= 3 :
    if m >= 7 :
        print(m - 2)
    elif m >= 4 :
        print(4)
    elif m >= 3 :
        print(3)
    elif m >= 2 :
        print(2)
    else :
        print(1)
elif n >= 2 :
    if m >= 7 :
        print(4)
    elif m >= 5 :
        print(3)
    elif m >= 3 :
        print(2)
    else :
        print(1)
else :
    print(1)