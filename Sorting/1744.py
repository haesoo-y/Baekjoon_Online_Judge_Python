import sys
input = sys.stdin.readline

def make_exp(lst):
    tmp = ''
    for i in range(len(lst)):
        if lst[i] == 1 or lst[i] == 0 :
            tmp += f'+{lst[i]}'
        elif i % 2 == 0 :
            tmp += f'+{lst[i]}'
        elif i % 2 == 1 :
            tmp += f'*{lst[i]}'
    return tmp

n = int(input())
lst_plus = []
lst_minus = []
for _ in range(n):
    num = int(input())
    if num < 0:
        lst_minus.append(num)
    else :
        lst_plus.append(num)
lst_plus.sort(reverse=True)
lst_minus.sort()
expression = make_exp(lst_plus) + make_exp(lst_minus)
if 0 in lst_plus and len(lst_minus) % 2 == 1:
    expression += '*0'
print(eval(expression))