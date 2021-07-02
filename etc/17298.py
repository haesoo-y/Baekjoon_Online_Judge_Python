import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
stack = []
answer = []
for num in lst[::-1] :
    while True :
        if not stack :
            answer.append(-1)
            stack.append(num)
            break
        if num >= stack[-1] :
            stack.pop()
        else :
            answer.append(stack[-1])
            stack.append(num)
            break

print(' '.join(map(str, answer[::-1])))