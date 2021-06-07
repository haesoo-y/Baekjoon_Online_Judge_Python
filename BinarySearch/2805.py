n, m = map(int, input().split())
trees = list(map(int,input().split()))
left = 0
right = max(trees)
answer = 0
while left <= right :
    mid = (left + right)//2
    num = 0
    for tree in trees :
        if tree > mid :
            num += tree - mid
        if num >= m :
            break
    if num >= m :
        answer = max(answer, mid)
        left = mid + 1
    else :
        right = mid - 1
print(answer)