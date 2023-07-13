n, m = map(int, input().split())
li = [*(input() for _ in range(n))]
ans = []
hd = 0

for i in range(m):
    d = {'A':0, 'C':0, 'G':0, 'T':0}
    for j in range(n):
        d[li[j][i]] += 1
    li_2 = sorted(d.items(), key= lambda x: (-x[1], x[0]))
    ans.append(li_2[0][0])
    hd += (n - li_2[0][1])

print(''.join(ans))
print(hd)