n = int(input())
cnt = 0
while True:
    if (cnt**2 + cnt) > n*2:
        break
    cnt += 1

print(cnt-1)