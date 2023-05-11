s = input().split('-')
for i in range(len(s)):
    p_split = s[i].split('+')
    s[i] = sum(map(int, p_split))

if len(s) != 1:
    for i in range(1, len(s)):
        s[0] -= s[i]

print(s[0])