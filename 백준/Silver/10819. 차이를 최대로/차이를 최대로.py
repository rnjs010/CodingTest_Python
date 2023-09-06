from itertools import permutations
import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = [*map(int, input().split())]
li = permutations(arr, n)

ans = 0
for i in li:
    s = 0
    for j in range(0, n-1):
        s += abs(i[j] - i[j+1])
    ans = max(ans, s)

print(ans)