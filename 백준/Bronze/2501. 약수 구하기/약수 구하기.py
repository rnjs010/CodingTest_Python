n, k = map(int, input().split())
li = []

for i in range(1, n+1):
    if n % i == 0:
        li.append(i)

print(0 if len(li) < k else li[k-1])