import sys
input = sys.stdin.readline

n = int(input())
dic = dict()

for i in range(n):
    lst = list(map(str, input().strip()))
    for j in range(len(lst)):
        ten_num = 10 ** ((len(lst)-j) - 1)
        if lst[j] in dic :
            dic[lst[j]] += ten_num
        else:
            dic[lst[j]] = ten_num
# print(dic) #{'G': 100, 'C': 1010, 'F': 1, 'A': 10000, 'D': 100, 'E': 10, 'B': 1}
x = sorted(dic.items(), key=lambda x:-x[1])
sum = 0
num = 9
for i in range(len(x)):
    sum += (num * x[i][1])
    num -= 1
print(sum)