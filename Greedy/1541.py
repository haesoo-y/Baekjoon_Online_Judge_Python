import sys
input = sys.stdin.readline

exp_lst = list(input().strip().split('-'))
for i in range(len(exp_lst)):
    exp = list(exp_lst[i].split('+'))
    for j in range(len(exp)):
        exp[j] = str(int(exp[j]))
    exp_lst[i] = f"({'+'.join(exp)})"
print(eval('-'.join(exp_lst)))
