import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = [''] * n
    for _ in range(n):
        x, y = map(int, input().split())
        index = x - 1
        lst[index] = [x, y]

    winner = 1
    win_num = lst[0][1]
    for i in range(1, n):
        if win_num > lst[i][1]:
            winner += 1
            win_num = lst[i][1]

    print(winner)
