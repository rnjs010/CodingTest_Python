import sys
input = sys.stdin.readline
n = int(input())
d = {i: 0 for i in input().rstrip().split()}

for _ in range(n):
    name = input().rstrip().split()
    for i in name:
        d[i] += 1

for i in sorted(d.items(), key= lambda x: -x[1]):
    print(*i)