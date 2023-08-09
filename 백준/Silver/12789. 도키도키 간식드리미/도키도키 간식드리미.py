n = int(input())
li = [*map(int, input().split())]

s = []
cnt = 1
for i in range(n):
    s.append(li[i])
    while s:
        if s[-1] == cnt:
            s.pop()
            cnt += 1
        else:
            break

print('Sad' if s else 'Nice')