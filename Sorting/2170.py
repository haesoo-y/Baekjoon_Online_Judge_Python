import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    x, y = map(int, input().split())
    lst.append([x, y])
lst.sort()
x, y = lst[0]
lines = [[x, y]]

for i in range(1, n):
    nx, ny = lst[i]
    if lines[-1][1] >= nx:
        if lines[-1][1] >= ny:
            continue
        else:
            lines[-1][1] = ny
    else :
        lines.append([nx, ny])

total = 0

for i in range(len(lines)):
    total += lines[i][1] - lines[i][0]

print(total)