lst = ['s', 't', 'u', 'd', 'y']
key = input('검색할 알파벳을 입력하시오 :')
i = 0
while True:
    if i == len(lst):
        idx = -1
        break
    if lst[i] == key:
        idx = i
        break
    i += 1
if idx == -1:
    print('찾는 알파벳이 존재하지 않습니다.')
else:
    print(f'검색하신 알파벳은 {idx + 1}번째에 있습니다.')

# 검색할 알파벳을 입력하시오 :d
# 검색하신 알파벳은 4번째에 있습니다.