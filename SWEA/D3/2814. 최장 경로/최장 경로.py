def dfs(n, visited):
    global ans
    ans = max(ans, len(visited))
    
    for v in li[n]:
        if v not in visited:
            dfs(v, visited + [v])


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    li = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        li[a].append(b)
        li[b].append(a)

    ans = 0
    for i in range(1, N + 1):
        dfs(i, [i])
    print(f'#{tc} {ans}')
