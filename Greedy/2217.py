n = int(input())
lst = list()
for _ in range(n):
    rope = int(input())
    lst.append(rope)

lst.sort()
lst.reverse()

for i in range(n):
    lst[i] = lst[i]*(i+1)

print(max(lst))