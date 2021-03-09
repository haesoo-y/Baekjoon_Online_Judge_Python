a, b = map(int, input().split())
lst = list()
i = 0
while len(lst) < b:
    i += 1
    lst += [i] * i

lst_slice = lst[a-1:b]
# print(lst)
# print(lst_slice)
print(sum(lst_slice))