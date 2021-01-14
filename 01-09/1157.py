counts = dict()
x = input().upper()
for i in x :
    counts[i] = counts.get(i, 0) + 1
max = max(counts.values())
multi = 0
for i in counts :
    if counts[i] == max :
        multi += 1
        answer = i
if multi > 1 :
    print('?')
else :
    print(answer)