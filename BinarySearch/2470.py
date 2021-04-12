import sys
input = sys.stdin.readline

def search(lst):
    start = 0
    end = len(lst) - 1
    z = abs(lst[start]+lst[end])
    z_start, z_end = start, end
    while start < end:
        tmp = lst[start]+lst[end]
        if abs(tmp) < z:
            z = abs(tmp)
            z_start, z_end = start, end
            if abs(tmp) == 0:
                return (z_start, z_end)
        if tmp < 0:
            start += 1
        else :
            end -= 1
    return (z_start, z_end)

n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
i1, i2 = search(n_lst)
print(n_lst[i1], n_lst[i2])