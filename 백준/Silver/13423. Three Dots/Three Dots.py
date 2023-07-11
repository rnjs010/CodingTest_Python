t = int(input())
for _ in range(t):
    cnt = 0
    n = int(input())
    li = sorted(list(map(int, input().split())))

    for i in range(n-1):
        for j in range(i+1, n):
            left = i
            right = j
            b = (li[left] + li[right]) / 2
            while left <= right:
                mid = (left + right) // 2
                if b == li[mid]:
                    cnt += 1
                    break
                elif b > li[mid]:
                    left = mid + 1
                elif b < li[mid]:
                    right = mid - 1
    print(cnt)