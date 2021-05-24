import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
answer = sum(lst) + 1
result = 0
for i in lst:
    if result + 1 < i:
        answer = result + 1
        break
    else :
        result += i
print(answer)