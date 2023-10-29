import sys
input = sys.stdin.readline

s = input().rstrip()
ans, a = 0, 0
for i in s:
    if i == '(':
        a += 1
    elif i == ')':
        if a > 0:
            a -= 1
        else:
            ans += 1
print(ans + a)