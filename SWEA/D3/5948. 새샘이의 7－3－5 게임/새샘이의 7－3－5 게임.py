sum_li = []
def combinations(arr, new_arr, n, c):
    if len(new_arr) == n:
        sum_li.append(sum(new_arr))
        return
    for i in range(c, 7):
        combinations(arr, new_arr + [arr[i]], n, i+1)


T = int(input())
for test_case in range(1, T + 1):
    sum_li = []
    li = list(map(int, input().split()))
    combinations(li, [], 3, 0)
    sort_li = sorted(list(set(sum_li)), reverse=True)
    print(f'#{test_case} {sort_li[4]}')