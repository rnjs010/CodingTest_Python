import sys, heapq
input = sys.stdin.readline

n = int(input())
li = [*map(int, input().split())]

d = dict()
for i in li:
    if i in d: d[i] += 1
    else: d[i] = 1

print(max(d.values()))