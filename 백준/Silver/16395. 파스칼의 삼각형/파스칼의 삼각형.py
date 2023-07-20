n, k = map(int, input().split())

if n in [1, 2]:
    print(1)
else:
    a = [1, 1]
    for i in range(3, n + 1):
        b = [1]
        for j in range(i - 2):
            b += [a[j] + a[j + 1]]
        b += [1]
        a = b
    print(b[k - 1])