import sys
input = sys.stdin.readline
num = 1
while True:
    s = input().rstrip()
    if '-' in set(s):
        break
    
    stack = [s[0]]
    for i in s[1:]:
        if stack:
            if i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    
    cnt = 0
    for i in range(0, len(stack), 2):
        cnt += (1 if stack[i] == stack[i+1] else 2)
    print(f'{num}. {cnt}')
    num += 1