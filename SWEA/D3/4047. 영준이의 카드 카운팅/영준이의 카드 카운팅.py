T = int(input())
for test_case in range(1, T + 1):
    all_card = {'S':13, 'D':13, 'H':13, 'C':13}
    get = {}
    li = input()
    check = 0
    for i in range(0, len(li)-2, 3):
        if li[i:i+3] in get:
            check = 1
            break
        else:
            get[li[i:i + 3]] = 1

        all_card[li[i:i+3][0]] -= 1

    if check == 1:
        print(f'#{test_case} ERROR')
    else:
        ans = ' '.join(map(str, list(all_card.values())))
        print(f'#{test_case} {ans}')