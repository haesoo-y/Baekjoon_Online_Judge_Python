for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    rplus = r1 + r2
    rminus = ((r2 - r1) ** 2) ** 0.5
    if d > rminus and d < rplus:
        print(2)
    elif d == rplus:
        print(1)
    elif d and d == rminus:
        print(1)
    elif d == 0 and r1 == r2:
        print(-1)
    else:
        print(0)

# 3
# 0 0 13 40 0 37
# 0 0 3 0 7 4
# 1 1 1 1 1 5