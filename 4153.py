while True :
    lst = list(map(int, input().split()))
    lst.sort()
    a = lst[0]
    b = lst[1]
    c = lst[2]
    if a==b==c==0 :
        break
    if (a*a)+(b*b) == (c*c) :
        print('right')
    else :
        print('wrong')


