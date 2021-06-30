def backtrack(lst, index):
    if lst[-1] > 0 :
        print(' '.join(map(str, lst)))
    else :
        for num in range(1, n+1):
            if visited[num]:
                continue
            visited[num] = True
            lst[index] = num
            backtrack(lst, index + 1)
            lst[index] = 0
            visited[num] = False


global n,m, visited
n, m = map(int, input().split())
answer = [0] * m
visited = [False] * (n+1)
backtrack(answer, 0)
