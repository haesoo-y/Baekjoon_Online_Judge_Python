n = int(input())
str_n = str(n)
len_n = len(str_n)
answer = 0
if n < 10 :
    answer = n
else :
    answer = (n - (10**(len_n-1)) + 1) * len_n
    for i in range(1, len_n):
        this_n = len_n - i
        answer += this_n * (10**this_n - 10**(this_n-1))
print(answer)