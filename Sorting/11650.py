n = int(input())
lst = list()
for i in range(n) :
    x, y = map(int, input().split())
    lst.append((x, y))

lst.sort()

for i in range(n):
    print(lst[i][0], lst[i][1])
