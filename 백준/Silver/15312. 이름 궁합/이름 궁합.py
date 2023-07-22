d = {'A':3,'E':3,'F':3,'H':3,'I':3, 'B':2,'D':2,'G':2,'J':2,
        'K':2,'M':2,'N':2,'P':2,'Q':2,'R':2,'T':2,'X':2,'Y':2, 
        'C':1,'L':1,'O':1,'S':1,'U':1,'V':1,'W':1,'Z':1}
a = input()
b = input()
li = []
for i, j in zip(a, b):
    li.append(d[i])
    li.append(d[j])

while True:
    li2 = []
    for i in range(len(li) - 1):
        li2 += [(li[i] + li[i + 1]) % 10]
    li = li2
    if len(li) == 2:
        print(''.join(map(str, li)))
        break