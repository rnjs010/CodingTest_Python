T = int(input())
for tc in range(1, T + 1):
    N = input()
    li, L = list(N), len(N)
    min_ans, max_ans = int(N), int(N)
    for i in range(L-1):
        for j in range(i+1, L):
            li[i], li[j] = li[j], li[i]
            if li[0] != '0':
                new_li = int(''.join(li))
                min_ans = min(min_ans, new_li)
                max_ans = max(max_ans, new_li)
            li[i], li[j] = li[j], li[i]
    print(f'#{tc} {min_ans} {max_ans}')