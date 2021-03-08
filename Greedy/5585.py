n = int(input())
r = 1000 - n
count = 0
for i in (500, 100, 50, 10, 5, 1) :
    if r // i > 0 :
        count += r // i
        r -= i * (r // i)

print(count)