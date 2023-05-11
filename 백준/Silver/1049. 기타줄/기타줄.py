n, m = map(int, input().split())
six = []
one = []
for _ in range(m):
    a, b = map(int, input().split())
    six.append(a)
    one.append(b)

six.sort()
one.sort()

print(min(six[0] * ((n // 6) + 1), six[0] * (n // 6) + one[0] * (n % 6), one[0] * n))