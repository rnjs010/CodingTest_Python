def dfs(i, sum_val):
    global cnt
    if k < sum_val: return  # 가지치기
    if i == n:
        if sum_val == k:
            cnt += 1
        return
    dfs(i+1, sum_val + li[i])   # 사용하는 경우
    dfs(i+1, sum_val)   # 사용하지 않는 경우


T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    cnt = 0
    dfs(0, 0)
    print(f'#{test_case} {cnt}')