import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = [*map(int, input().split())]

arr = [0] * m
s = 0
for i in li:
    s += i
    arr[s % m] += 1

cnt = arr[0]
for i in arr:
    cnt += i*(i-1)//2

print(cnt)