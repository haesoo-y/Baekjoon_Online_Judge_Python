import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    word = str(input().strip())
    c = len(word)
    lst.append((word, c))

lst = list(set(lst))

lst.sort(key = lambda x: (x[1], x[0]))

for i in lst:
    print(i[0])