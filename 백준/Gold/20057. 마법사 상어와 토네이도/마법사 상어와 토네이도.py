import sys
input = sys.stdin.readline
n = int(input())
arr = [[0]*(n+1)] + [[0] + [*map(int, input().split())] for _ in range(n)]
ans = 0

def func(y, x, dy, dx):
    global ans
    sum = 0
    div = [0.01, 0.01, 0.07, 0.07, 0.02, 0.02, 0.1, 0.1, 0.05]
    for i in range(10):
            ny = dy[i]
            nx = dx[i]
            if ny < 1 or ny > n or nx < 1 or nx > n:
                if i == 9: ans += (arr[y][x] - sum)
                else:
                    ans += int(arr[y][x] * div[i])
                    sum += int(arr[y][x] * div[i])
                continue
            if i == 9: arr[ny][nx] += (arr[y][x] - sum)
            else:
                arr[ny][nx] += int(arr[y][x] * div[i])
                sum += int(arr[y][x] * div[i])
    arr[y][x] = 0

def wind(y, x, dir):
    if dir == 0:
        dy = [y + 1, y - 1, y + 1, y - 1, y + 2, y - 2, y + 1, y - 1, y, y]
        dx = [x + 1, x + 1, x, x, x, x, x - 1, x - 1, x - 2, x - 1]
        func(y, x, dy, dx)
    elif dir == 1:
        dy = [y + 1, y - 1, y + 1, y - 1, y + 2, y - 2, y + 1, y - 1, y, y]
        dx = [x - 1, x - 1, x, x, x, x, x + 1, x + 1, x + 2, x + 1]
        func(y, x, dy, dx)
    elif dir == 2:
        dy = [y - 1, y - 1, y, y, y, y, y + 1, y + 1, y+2, y+1]
        dx = [x - 1, x + 1, x + 1, x - 1, x + 2, x - 2, x + 1, x - 1, x, x]
        func(y, x, dy, dx)
    else:
        dy = [y + 1, y + 1, y, y, y, y, y - 1, y - 1, y - 2, y - 1]
        dx = [x - 1, x + 1, x + 1, x - 1, x + 2, x - 2, x + 1, x - 1, x, x]
        func(y, x, dy, dx)

dist = 1
cnt = 0
dir = 0
y = (n // 2) + 1
x = y
while x != 1 or y != 1:
    if dir == 0: x -= 1
    elif dir == 1: x += 1
    elif dir == 2: y += 1
    else: y -= 1
    wind(y, x, dir)
    cnt += 1
    if cnt == dist:
        cnt = 0
        if dir == 0: dir = 2
        elif dir == 2: dir = 1
        elif dir == 1: dir = 3
        else: dir = 0
        if dir == 1 or dir == 0: dist += 1

print(ans)