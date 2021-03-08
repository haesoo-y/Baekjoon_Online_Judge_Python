lst = list(map(str, input()))
lst_r = lst.copy()
lst_r.reverse()
if lst == lst_r :
    print(1)
else :
    print(0)