n, k = map(int, input().split())
li = [*map(int, input().split())]
ans = 0
used = [0] * n

def kit(x, weight):
    global ans
    if x == n:
        ans += 1
        return

    for i in range(n):
        if used[i] == 0 and weight + (li[i] - k) >= 500:
            used[i] = 1
            kit(x + 1, weight + (li[i] - k))
            used[i] = 0

kit(0, 500)
print(ans)