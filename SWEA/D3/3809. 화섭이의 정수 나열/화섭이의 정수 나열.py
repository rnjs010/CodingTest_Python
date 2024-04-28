T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_str = ''
    while True:
        num_str += ''.join(list(input().split()))
        if len(num_str) == N: break
        
    num, ans = 0, 0
    while True:
        if str(num) not in num_str:
            ans = num
            break
        num += 1

    print(f'#{test_case} {ans}')