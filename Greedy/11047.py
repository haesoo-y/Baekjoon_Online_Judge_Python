n, k = map(int, input().split())
lst = list()
count = 0
for i in range(n) :
    lst.append(int(input()))

lst.reverse()

for i in lst :
    if k >= i :
        count += k//i
        k = k % i

print(count)