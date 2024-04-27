def check(s):
    if s == s[-1::-1]:
        return True
    return False

T = int(input())
for test_case in range(1, T + 1):
    S = input()
    ans = ''
    if check(S) and check(S[:len(S)//2]) and check(S[len(S)//2+1:]):
        ans = 'YES'
    else:
        ans = 'NO'
    print(f'#{test_case} {ans}')