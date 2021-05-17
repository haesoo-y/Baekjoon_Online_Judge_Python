import sys
input = sys.stdin.readline
while True:
    num = input().strip()
    if num == '0' :
        break
    half_len = len(num)//2
    num_len = len(num)
    result = 'yes'
    for i in range(half_len):
        if num[i] != num[num_len - 1 - i]:
            result = 'no'
            break
    print(result)