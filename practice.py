def recur(n) :
    if n > 0 :
        recur(n - 1)
        print(n)
        recur(n - 2)

x = int(input('입력 : '))
recur(x)

# 입력 : 3
# 1
# 2
# 3
# 1