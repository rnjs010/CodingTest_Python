import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(input().rstrip())

cnt = 0
for i in range(n):
    if li[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if li[j] == 'H':
                cnt += 1
                li[j] = 0
                break

print(cnt)