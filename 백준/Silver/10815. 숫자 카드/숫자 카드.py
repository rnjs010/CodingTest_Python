n = int(input())
li = set(input().split())
m = int(input())
li2 = list(input().split())

for i in li2:
    if i in li:
        print(1, end=' ')
    else:
        print(0, end=' ')
