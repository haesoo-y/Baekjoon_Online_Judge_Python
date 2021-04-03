import sys
input = sys.stdin.readline
def sum_num(string):
    sum = 0
    for i in string:
        if i.isdigit():
            sum += int(i)
    return sum

def is_big(x, y): # x가 더 크면 True
    # 1. 길이 비교
    if len(x) > len(y) :
        return True
    elif len(x) < len(y) :
        return False
    # 2. 자리 수 합 비교
    if sum_num(x) > sum_num(y):
        return True
    elif sum_num(x) < sum_num(y):
        return False
    # 3. 사전 순 비교
    if x > y :
        return True
    else:
        return False

n = int(input())
lst = list()
for _ in range(n):
    lst.append(input().strip())

# print(lst) # ['ABCD', '145C', 'A', 'A910', 'Z321']

for i in range(n - 1):
    for j in range(i+1, n):
        if is_big(lst[i], lst[j]): # 기준(lst[i]이 더 크면 스왑
            lst[i], lst[j] = lst[j], lst[i]

# print(lst) # ['A', 'ABCD', 'Z321', '145C', 'A910']

for i in lst:
    print(i)