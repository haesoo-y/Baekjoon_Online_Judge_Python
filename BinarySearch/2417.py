import sys

def binary_search(x):
    start = 0
    end = x
    tmp = 0
    while start <= end:
        mid = (start + end) // 2
        if mid ** 2 >= x:
            tmp = mid
            end = mid - 1
        else:
            start = mid + 1
    return tmp

input = sys.stdin.readline

n = int(input())
answer = binary_search(n)
print(answer)