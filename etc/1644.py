import sys
input = sys.stdin.readline

n = int(input())
prime_bool = [True] * (n+1)
prime_bool[0], prime_bool[1] = False, False
for i in range(2, int(n**1/2) + 1):
    if prime_bool[i]:
        j = 2
        while i * j <= n:
            prime_bool[i * j] = False
            j += 1
prime_lst = []
# 소수 리스트 만들기
for i in range(2, n+1):
    if prime_bool[i]:
        prime_lst.append(i)
# [2, 3, 5, 7, 11, 13, 17, 19]

# 투포인터 이용해서 합이 n인 경우 세기
count = 0
end = 0
interval_sum = 0
for start in range(0, len(prime_lst)):
    while interval_sum < n and end < len(prime_lst):
        interval_sum += prime_lst[end]
        end += 1
    if interval_sum == n:
        count += 1
    interval_sum -= prime_lst[start]
print(count)