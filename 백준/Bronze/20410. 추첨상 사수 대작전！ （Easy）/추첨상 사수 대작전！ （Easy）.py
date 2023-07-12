m, seed, x, y = map(int, input().split())

for a in range(1, m):
    for c in range(1, m):
        if (a * seed + c) % m == x and (a * x + c) % m == y:
            print(a, c)
            exit()