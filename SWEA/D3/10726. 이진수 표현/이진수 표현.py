T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    bin_num = format(m, 'b')
    ans = ''
    if n > len(bin_num):
        ans = 'OFF'
    else:
        ans = 'ON' if bin_num[-n:] == ('1' * n) else 'OFF'
    print(f'#{test_case} {ans}')