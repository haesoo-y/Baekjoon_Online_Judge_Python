A, B, C = map(int,input().split())
p = C-B
q = 0
if p > 0 :
    q = (A//p) + 1
else :
    q = -1
print(q)

