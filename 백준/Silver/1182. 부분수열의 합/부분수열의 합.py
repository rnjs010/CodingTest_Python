import sys
input = sys.stdin.readline
n, s = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0

def dfs(idx, total):
    global cnt
    if idx >= n:
        return

    total += li[idx]
    if total == s:
        cnt += 1

    dfs(idx+1, total - li[idx])
    dfs(idx+1, total)

dfs(0, 0)
print(cnt)