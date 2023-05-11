a, b = map(int, input().split())
cnt = 0
while a != b:
    cnt += 1
    c = b
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    if c == b or a > b:
        print(-1)
        break
else:
    print(cnt+1)