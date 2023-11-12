import sys
input = sys.stdin.readline

n, s, r = map(int, input().split())
x_li = sorted([*map(int, input().split())])
o_li = sorted([*map(int, input().split())])

temp = x_li.copy()
for i in temp:
    if i in o_li:
        o_li.remove(i)
        x_li.remove(i)

li = [1] * (n+1)
for i in x_li: li[i] = 0
for i in o_li: li[i] = 2

for i in range(1, n+1):
    if li[i] == 0:
        if i == n:
            if li[i-1] == 2:
                li[i], li[i-1] = 1, 1
                break
        else:
            if li[i-1] == 2:
                li[i], li[i-1] = 1, 1
                continue
            if li[i+1] == 2:
                li[i], li[i+1] = 1, 1
                continue

print(li.count(0))