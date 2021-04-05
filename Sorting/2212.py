import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
lst = list(map(int, input().split()))
lst.sort()
m_lst = []
for i in range(1, n):
    m_lst.append(lst[i]-lst[i-1])
m_lst.sort()
if k >= n :
    m_lst = [0]
elif k > 1 :
    for _ in range(k - 1):
        m_lst.pop()
print(sum(m_lst))