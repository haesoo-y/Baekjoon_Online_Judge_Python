L, P, V = map(int, input().split())
i = 0
while L > 0 and P > 0 and V > 0 :
    i += 1
    plus = min(L, V%P)
    answer = (V // P)*L + plus
    print(f'Case {i}:', answer)
    L, P, V = map(int, input().split())
