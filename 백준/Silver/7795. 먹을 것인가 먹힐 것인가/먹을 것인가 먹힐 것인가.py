t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a_li = list(map(int, input().split()))
    b_li = list(map(int, input().split()))

    b_li.sort()
    result = 0
    for a in a_li:
        cnt = -1
        start, end = 0, m-1
        while start <= end:
            mid = (start + end ) // 2
            if a > b_li[mid]:
                cnt = max(cnt, mid)
                start = mid + 1
            else:
                end = mid - 1
        result += (cnt+1)

    print(result)