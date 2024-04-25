for test_case in range(1, 11):
    n = int(input())
    li = [list(input().split()) for _ in range(100)]
    ans = 0
    for i in range(100):
        s = ''
        for j in range(100):
            if li[j][i] != '0':
                s += li[j][i]
        ans += s.count('12')

    print(f'#{test_case} {ans}')