import sys, math
input = sys.stdin.readline

def r(x):
    return int(x) + 1 if x % 1 >= 0.5 else int(x)

n = int(input())
li = sorted([int(input()) for _ in range(n)])

a = r(n * 0.15)
print(0 if n == 0 else r(sum(li[a:n-a]) / (n - 2 * a)))