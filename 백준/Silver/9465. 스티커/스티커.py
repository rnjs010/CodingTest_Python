t = int(input())
for _ in range(t):
    n = int(input())
    li = []
    for i in range(2):
        li.append([*map(int, input().split())])
    
    for j in range(1, n):
        if j == 1:
            li[0][j] += li[1][0]
            li[1][j] += li[0][0]
        else:
            li[0][j] += max(li[1][j - 1], li[1][j - 2])
            li[1][j] += max(li[0][j - 1], li[0][j - 2])
    
    print(max(li[0][-1], li[1][-1]))