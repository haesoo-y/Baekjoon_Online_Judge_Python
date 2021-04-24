import sys
input = sys.stdin.readline

t = int(input())

if t % 10 > 0 :
    print(-1)
    quit()

print(t//300, end=' ')
t %= 300
print(t//60, end=' ')
t %= 60
print(t//10)
