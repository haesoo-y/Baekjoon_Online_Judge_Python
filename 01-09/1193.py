X = int(input())
g = 1 # 그룹의 번호
i = 1 # 그룹에서의 마지막 인덱스
while X > i :
    g += 1
    i += g
# 분자 : N
# 분모 : D
G_index = g - (i - X) # 그룹 내에서의 인덱스
if g%2 == 0 : # 짝수 그룹일 경우
    N = G_index
    D = g - (G_index-1)
else : # 홀수 그룹일 경우
    D = G_index
    N = g - (G_index - 1)

print('{}/{}'.format(N,D))
