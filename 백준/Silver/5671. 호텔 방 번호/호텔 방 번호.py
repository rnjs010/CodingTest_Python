while True:
    try:
        n, m = map(int, input().split())
        ans = 0

        for i in range(n, m + 1):
            s = set()
            for j in str(i):
                s.add(j)
            if len(s) == len(str(i)):
                ans += 1
        
        print(ans)
    except:
        break