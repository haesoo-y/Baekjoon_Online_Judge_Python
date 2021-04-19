import sys
from math import factorial
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    answer = factorial(m)//(factorial(n)*factorial(m-n))
    print(answer)