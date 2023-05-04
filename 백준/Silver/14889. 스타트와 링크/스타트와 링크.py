import sys
input = sys.stdin.readline
n = int(input())
s_li = []
for _ in range(n):
    s_li.append(list(map(int, input().split())))

p_li = range(1,n+1)
team = [0]*(n//2)
min_v = []
def dfs(depth, beginWidth):
    global min_v
    if depth == (n//2):
        s_sum = 0
        for j in team:
            for k in team:
                s_sum += s_li[j-1][k-1]
        min_v.append(s_sum)
    else:
        for i in range(beginWidth, len(p_li)):
            team[depth] = p_li[i]
            dfs(depth+1, i+1)

dfs(0,0)
answer = sys.maxsize
for i in range(len(min_v)):
    answer = min(answer, abs(min_v[i] - min_v[-(i+1)]))
print(answer)