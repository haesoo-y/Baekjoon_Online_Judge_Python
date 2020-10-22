lst = list()
for i in range(10):
    lst.append(int(input())%42)
# print(lst)
cnt = dict()
for n in lst :
    cnt[n] = cnt.get(n, 0) + 1
# print(cnt)
print(len(cnt))

# [39, 40, 41, 0, 1, 2, 40, 41, 0, 1]
# {39: 1, 40: 2, 41: 2, 0: 2, 1: 2, 2: 1}
# 6
