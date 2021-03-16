def dfs(list, visited, n) :
    visited[n] = True
    for i in list[n] :
        if not visited[i] :
            dfs(list, visited, i)


computer = int(input())
linked = int(input())
lst = [[] for i in range(computer+1)]

for _ in range(linked) :
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

visited = [False] * (computer + 1)
dfs(lst, visited, 1)
print(visited.count(True) - 1)
