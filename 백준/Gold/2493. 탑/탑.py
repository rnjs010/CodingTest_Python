import sys
input = sys.stdin.readline
n = int(input().rstrip())
li = list(map(int, input().rstrip().split()))
answer = []
s = []
for i in range(n):
    while s:
        if s[-1][1] > li[i]:
            answer.append(s[-1][0])
            break
        else:
            s.pop()
    else:
        answer.append(0)
    s.append([i+1, li[i]])

print(' '.join(map(str, answer)))