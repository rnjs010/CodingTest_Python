import sys
input = sys.stdin.readline
from itertools import combinations
n, k = map(int, input().split())
li = [[*map(int, input().split())] for _ in range(n)]

ans = []
for x in combinations(range(n), k):
    total = 0
    for i in range(k-1):
        for j in range(i+1, k):
            total += li[x[i]][x[j]]
    ans.append(total)

print(max(ans))