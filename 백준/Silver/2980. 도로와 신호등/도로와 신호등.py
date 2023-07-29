n, l = map(int, input().split())
dis = [0]
time = 0
for _ in range(n):
    d, r, g = map(int, input().split())
    time += d - dis[-1]
    dis.append(d)
    if time % (r + g) < r:
        time += (r - (time % (r + g)))

print(time + (l - dis[-1]))