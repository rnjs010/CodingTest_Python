for test_case in range(10):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    for i in li:
        ans = max(ans, sum(i))

    for i in range(100):
        temp = 0
        for j in range(100):
            temp += li[j][i]
        ans = max(ans, temp)

    temp = 0
    for i in range(100):
        temp += li[i][i]
    ans = max(ans, temp)

    temp = 0
    for i in range(100):
        temp += li[i][99-i]
    ans = max(ans, temp)

    print(f'#{n} {ans}')
