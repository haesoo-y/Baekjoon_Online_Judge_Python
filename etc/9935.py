import sys
input = sys.stdin.readline

string = input().strip()
e = input().strip()
last_e = e[-1]
length = len(e)
stack = []
for s in string:
    stack += s
    if last_e == s and ''.join(stack[-length :]) == e:
        del stack[-length:]

print(''.join(stack) if stack else 'FRULA')