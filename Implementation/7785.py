import sys
input = sys.stdin.readline
n = int(input())
company = {}
for _ in range(n):
    name, check = map(str, input().strip().split())
    if check == 'enter':
        company[name] = True
    else :
        del company[name]

lst = sorted(company.keys(), reverse=True)
for name in lst:
    print(name)