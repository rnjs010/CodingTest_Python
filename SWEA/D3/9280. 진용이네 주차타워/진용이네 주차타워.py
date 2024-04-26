from collections import deque
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    p_money = [0] + [int(input()) for _ in range(n)]
    car_weight = [0] + [int(input()) for _ in range(m)]
    ans = 0
    parking = [0] * (n + 1)
    order = deque([int(input()) for _ in range(2*m)])
    waiting = deque([])
    while True:
        if not order and not waiting: break
        num = order.popleft()
        if num > 0:
            for i in range(1, n + 1):
                if parking[i] == 0:
                    parking[i] = num
                    ans += (p_money[i] * car_weight[num])
                    break
            else:
                waiting.append(num)
        else:
            idx = parking.index(-num)
            parking[idx] = 0
            if waiting:
                num = waiting.popleft()
                parking[idx] = num
                ans += (p_money[idx] * car_weight[num])

    print(f'#{test_case} {ans}')