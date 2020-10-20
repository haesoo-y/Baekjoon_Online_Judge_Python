A = int(input())
B = int(input())
C = int(input())
N = A * B * C

lst = list(i for i in str(N))

for i in range(10) :
    print(lst.count(str(i)))
