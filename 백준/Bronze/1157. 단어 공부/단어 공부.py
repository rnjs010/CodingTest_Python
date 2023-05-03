n = input()
n = list(n.upper())

new_li = list(set(n))
c = []
for i in new_li:
    c.append(n.count(i))

if c.count(max(c)) >= 2:
    print('?')
else:
    print(new_li[c.index(max(c))])
