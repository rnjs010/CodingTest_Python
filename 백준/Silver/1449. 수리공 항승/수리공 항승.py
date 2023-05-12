n, l = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
start = li[0]
cnt = 1
for i in li[1:]:
    if i > start + (l - 1):
        cnt += 1
        start = i

print(cnt)