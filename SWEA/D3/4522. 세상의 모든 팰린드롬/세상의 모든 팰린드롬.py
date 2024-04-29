T = int(input())
for tc in range(1, T + 1):
    word = input()
    re_word = word[::-1]
    half = len(word) // 2
    ans = 'Exist'
    for i in range(half):
        if word[i] != re_word[i]:
            if word[i] != '?' and re_word[i] != '?':
                ans = 'Not exist'
                break

    print(f'#{tc} {ans}')