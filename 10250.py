T = int(input())
for _ in range(T) :
    H, W, N = map(int, input().split())
    XX = str((N-1)//H + 1).zfill(2)
    YY = str((N-1)%H + 1)
    print(YY + XX)