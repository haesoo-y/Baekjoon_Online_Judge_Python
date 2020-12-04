A, B, V = map(int,input().split())
T = V-A
if T%(A-B) == 0 :
    d = T/(A-B) + 1
else :
    d = T//(A - B) + 2
print(int(d))

