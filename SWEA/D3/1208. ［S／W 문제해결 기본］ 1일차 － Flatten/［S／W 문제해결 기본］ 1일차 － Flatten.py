for test_case in range(1, 11):
    n = int(input())
    li = list(map(int, input().split()))
    cnt = [0] * 101
    for i in li:
        cnt[i] += 1
    
    max_val, min_val = 0, 0
    for _ in range(n):
        for i in range(101):
            if cnt[i] != 0:
                cnt[i] -= 1
                cnt[i+1] += 1
                min_val = i+1 if cnt[i] == 0 else i
                break
        
        for i in range(100, 0, -1):
            if cnt[i] != 0:
                cnt[i] -= 1
                cnt[i-1] += 1
                max_val = i - 1 if cnt[i] == 0 else i
                break
        
    print(f'#{test_case} {max_val-min_val}')
