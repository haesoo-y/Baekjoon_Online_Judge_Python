import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = []
accum_table = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n):
    table.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        accum_table[i][j] = accum_table[i][j-1] + table[i-1][j-1]
for i in range(1, n+1):
    for j in range(1, n+1):
        accum_table[i][j] = accum_table[i-1][j] + accum_table[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = accum_table[x2][y2] - accum_table[x2][y1 - 1] - accum_table[x1 - 1][y2] + accum_table[x1-1][y1-1]
    print(answer)
