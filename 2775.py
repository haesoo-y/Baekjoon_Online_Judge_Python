lst = list()
for _ in range(15) :
    lst.append(list())
lst[0] = [i for i in range(15)]
# print('0 층 : ', lst[0])
for i in range(1,15) :
    lst[i].append(0)
    for j in range(1,14) :
        lst[i].append(lst[i][j-1]+lst[i-1][j])
    # print(i,'층 :',lst[i])
T = int(input())
for _ in range(T) :
    k = int(input())
    n = int(input())
    print(lst[k][n])