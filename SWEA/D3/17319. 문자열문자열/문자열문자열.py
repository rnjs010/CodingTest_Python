T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    S = input()
    ans = ''
    ans = 'Yes' if N % 2 == 0 and S[:N//2] == S[N//2:] else 'No'
    print(f'#{test_case} {ans}')