N = int(input())
X = N
i = 0
while True :
    a = X // 10
    b = X % 10
    c = a + b
    X = (b*10)+(c%10)
    i = i +1
    if X == N :
        break
print(i)

