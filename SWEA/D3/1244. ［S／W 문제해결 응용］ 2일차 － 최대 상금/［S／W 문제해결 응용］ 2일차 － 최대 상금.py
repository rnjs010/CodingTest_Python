def dfs(n):
    global ans
    if n == int(M):
        ans = max(ans, int(''.join(li)))
        return
    for i in range(L-1):
        for j in range(i + 1, L):
            li[i], li[j] = li[j], li[i]
            chk = ''.join(li)
            if (n, chk) not in visited:
                dfs(n + 1)
                visited[(n, chk)] = 1
            li[i], li[j] = li[j], li[i]


T = int(input())
for tc in range(1, T + 1):
    S, M = input().split()
    li, L, ans = list(S), len(S), 0
    visited = {}
    dfs(0)
    print(f'#{tc} {ans}')