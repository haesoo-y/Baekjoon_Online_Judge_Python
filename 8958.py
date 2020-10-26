N = int(input())
for i in range(N) :
    prbm = input()
    add = 0
    score = 0
    for i in range(len(prbm)) :
        if prbm[i] == 'O' and prbm[i-1] == 'O' :
            add = add + 1
        elif prbm[i] == 'O' :
            add = 1
        else :
            add = 0
        score = score + add
    print(score)