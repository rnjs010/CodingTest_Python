while True:
    n = int(input())
    if n == -1:
        break
    
    li = []
    d = 1
    while d < n:
        if n % d == 0:
            li.append(d)
        d += 1

    if sum(li) != n:
        print(f'{n} is NOT perfect.')
    else:
        print(n, '=', ' + '.join(map(str, li)))