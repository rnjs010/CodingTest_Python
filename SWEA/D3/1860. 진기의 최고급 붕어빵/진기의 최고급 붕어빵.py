import heapq

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    li = list(map(int, input().split()))
    heapq.heapify(li)
    last_time = li[-1]
    make = 0
    ans = ''
    for i in range(last_time + 1):
        if i != 0 and i % M == 0:
            make += K
        if li[0] == i:
            if make > 0:
                make -= 1
                heapq.heappop(li)
            else:
                ans = 'Impossible'
                break
    else:
        ans = 'Possible'

    print(f'#{test_case} {ans}')