import sys
input = sys.stdin.readline
n = int(input())
words = [input().rstrip() for _ in range(n)]
d = {}
for word in words:
    i = len(word) - 1
    for s in word:
        if s in d:
            d[s] += 10**i
        else:
            d[s] = 10**i
        i -= 1

total, num = 0, 9
for i in sorted(d.values(), reverse=True):
    total += i * num
    num -= 1

print(total)