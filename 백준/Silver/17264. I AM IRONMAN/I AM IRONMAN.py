import sys
input = sys.stdin.readline

n, p = map(int, input().split())
w, l, g = map(int, input().split())

d = dict()
for _ in range(p):
    a, b = input().rstrip().split()
    d[a] = b

total, ch = 0, 0
for _ in range(n):
    player = input().rstrip()
    total += (-l if player not in d or d[player] == 'L' else w)
    if total < 0: total = 0
    if total >= g: ch = 1

print('I AM NOT IRONMAN!!' if ch == 1 else 'I AM IRONMAN!!')