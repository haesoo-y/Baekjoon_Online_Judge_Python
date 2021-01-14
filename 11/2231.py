# 분해합 구하기
def deSum(n) :
    numstr = str(n)
    s = n
    for i in range(len(numstr)) :
        s = s + int(numstr[i])
    return s

# 생성자 찾기
def findCon(m) :
    for i in range(m) :
        if m == deSum(i) :
            return i
    return 0

N = int(input())
print(findCon(N))

