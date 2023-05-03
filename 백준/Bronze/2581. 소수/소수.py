a = int(input())
b = int(input())
li = []
def check(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

for i in range(a,b+1):
    if check(i) == True:
        li.append(i)

if len(li) > 0:
    print(sum(li))
    print(li[0])
else:
    print(-1)