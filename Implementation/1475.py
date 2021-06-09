def create_cards(d):
    for i in range(10):
        if i == 9 :
            i = 6
        d[str(i)] = d.get(str(i), 0) + 1

n = input()
dic = dict()
# 9는 모두 6으로 통일
count = 0
for c in n:
    if c == '9':
        c = '6'
    if dic.get(c):
        dic[c] -= 1
    else :
        count += 1
        create_cards(dic)
        dic[c] -= 1
print(count)
