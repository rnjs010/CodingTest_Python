n = int(input())

ch = 0
while True:
    if 2**ch >= n:
        break
    ch += 1

cut = 0
if 2**ch == n:
    print(n, 0)
else:
    for i in range(ch-1, -1, -1):
        if n < 2**i:
            if n != 0:
                cut += 1
                continue
            if n == 0:
                break
        cut += (n // (2**i))
        n %= (2**i)
    print(2**ch, cut)