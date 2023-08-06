import sys
input = sys.stdin.readline

s = input().rstrip()
li = [{}]
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
    temp = {k: v for k, v in d.items()}
    li.append(temp)

n = int(input())
for _ in range(n):
    q = input().rstrip().split()
    print(li[int(q[2])+1].get(q[0],0) - li[int(q[1])].get(q[0],0))