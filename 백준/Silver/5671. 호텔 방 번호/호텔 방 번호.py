while True:
    try:
        n, m = map(int, input().split())
        ans = 0

        for i in range(n, m + 1):
            li = [0] * 10
            for j in str(i):
                li[int(j)] += 1
                if (2 in li) or (3 in li) or (4 in li):
                    break
            else:
                ans += 1
        
        print(ans)
    except:
        break