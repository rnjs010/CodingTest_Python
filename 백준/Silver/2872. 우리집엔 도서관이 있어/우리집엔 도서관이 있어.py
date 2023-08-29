import sys, heapq
input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)]

a, cnt = n, 0
for i in range(li.index(n), -1, -1):
    if li[i] == a:
        a -= 1
        cnt += 1

print(len(li) - cnt)