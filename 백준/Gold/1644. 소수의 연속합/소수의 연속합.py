n = int(input())

ch = [False, False] + [True] * (n-1)
prime = []
for i in range(2, n+1):
    if ch[i]:
        prime.append(i)
        for j in range(2*i, n+1, i):
            ch[j] = False

s, e, ans = 0, 0, 0
while e <= len(prime):
    t = sum(prime[s:e])
    if t == n:
        ans += 1
        e += 1
    elif t < n:
        e += 1
    else:
        s += 1

print(ans)