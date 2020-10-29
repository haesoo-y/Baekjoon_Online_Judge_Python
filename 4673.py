lst = list()
for i in range(10001) :
    if i < 10 :
        lst.append(i+i)
    elif i < 100 :
        lst.append(i + i//10 + i%10)
    elif i < 1000 :
        lst.append(i + i//100 + (i%100)//10 + (i%100)%10)
    else :
        n = i + i//1000 + (i%1000)//100 + ((i%1000)%100)//10 + ((i%1000)%100)%10
        if n < 10001 :
            lst.append(n)
for i in range(10001) :
    if i not in lst :
        print(i)