n = int(input())
c = int(input())
lst = list(map(int, input().split()))
p_lst = [0] * n # 사진틀
c_lst = [0] * n # 추천 받은 수
for i in lst :
    if i in p_lst: # 사진틀에 이미 있으면
        index = p_lst.index(i)
        c_lst[index] += 1

    else : # 사진틀에 없으면 (새로운 후보이면)
        if 0 in p_lst : # 사진틀에 빈공간이 있으면
            index = p_lst.index(0)
            p_lst[index] = i
            c_lst[index] = 1

        else : # 사진틀에 빈공간이 없으면
            index = c_lst.index(min(c_lst))
            p_lst.pop(index)
            c_lst.pop(index)
            p_lst.append(i)
            c_lst.append(1)
p_lst.sort()
for i in p_lst :
    print(i, end=' ')


