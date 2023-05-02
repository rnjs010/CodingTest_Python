import sys
input = sys.stdin.readline
word = input().rstrip()
n = int(input())
s = []
for i in word:
    s.append(i)

li = []
for _ in range(n):
    command = input().rstrip().split()
    if command[0] == 'L':
        if s:
            li.append(s.pop())
    elif command[0] == 'D':
        if li:
            s.append(li.pop())
    elif command[0] == 'B':
        if s:
            s.pop()
    else:
        s.append(command[1])

for _ in range(len(li)):
    s.append(li.pop())

print(''.join(s))