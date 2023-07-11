import sys
input = sys.stdin.readline
r, c = map(int, input().split())
li = []
for _ in range(r):
    li.append(list(map(int, input().split())))
t = int(input())

new_i = []
for z in range(0, r-2):
    for i in range(0, c-2):
        f = []
        for j in range(z, z+3):
            f += li[j][i:i+3]
        f.sort()
        if f[4] >= t:
            new_i.append(f[4])

print(len(new_i))