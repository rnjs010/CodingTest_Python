T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    ans = 1 + (n * 4)
    for x in range(1, n):
        for y in range(1, n):
            if x**2 + y**2 <= n**2:
                ans += 4
    print(f'#{test_case} {ans}')
