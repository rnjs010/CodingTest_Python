t = int(input())
li = [0] * 12
li[1], li[2], li[3] = 1, 2, 4

for i in range(4, 12):
    li[i] = sum(li[i-3:i])

for _ in range(t):
    n = int(input())
    print(li[n])