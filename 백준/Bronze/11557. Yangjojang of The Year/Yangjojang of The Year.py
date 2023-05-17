import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    li = []
    for _ in range(n):
        a, b = input().rstrip().split()
        li.append((a, int(b)))
    
    li.sort(key=lambda x: x[1])
    print(li[-1][0])