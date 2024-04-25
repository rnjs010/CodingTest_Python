T = int(input())
num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for test_case in range(1, T + 1):
    tc, n = input().split()
    li = list(input().split())
    d = {}
    for i in li:
        if i in d: d[i] += 1
        else: d[i] = 1

    print(f'#{test_case}')
    for number in num:
        if number in d:
            for i in range(d[number]):
                print(number, end=' ')
    print()