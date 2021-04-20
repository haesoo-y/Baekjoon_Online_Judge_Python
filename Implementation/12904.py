import sys
input = sys.stdin.readline

s = list(map(str, input().strip()))
t = list(map(str, input().strip()))

while len(s) < len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()

if s == t :
    print(1)
else :
    print(0)
