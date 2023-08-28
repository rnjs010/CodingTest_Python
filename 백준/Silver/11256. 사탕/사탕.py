import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    li = []
    for _ in range(m):
        a, b = map(int, input().split())
        li.append(a*b)
    
    li.sort(reverse=True)
    for i in range(m):
        n -= li[i]
        if n <= 0:
            print(i+1)
            break