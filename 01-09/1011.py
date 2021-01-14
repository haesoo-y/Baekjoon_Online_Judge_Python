import math

T = int(input())
for _ in range(T) :

    x, y = map(int,input().split())
    D = y-x
    D_root = int(math.sqrt(D-1)) #거리-1 의 루트값 정수부분
    D_group = D_root**2 #D_root의 제곱값

    if D > D_root + D_group :
        count = 2*D_root + 1
    else :
        count = 2*D_root

    if D < 4 :
        count = D

    print(count)
