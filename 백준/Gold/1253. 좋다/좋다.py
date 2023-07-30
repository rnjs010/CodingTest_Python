n = int(input())
li = sorted([*map(int, input().split())])
cnt = 0

for i in range(n):
    arr = li[:i] + li[i + 1:]
    l, r = 0, len(arr) - 1
    while l < r:
        if li[i] == arr[l] + arr[r]:
            cnt += 1
            break
        elif li[i] > arr[l] + arr[r]:
            l += 1
        else:
            r -= 1

print(cnt)