n = int(input())
row = [0] * n
ans = 0

def check(x):
    for i in range(x):
        if (row[x] == row[i]) or (abs(x - i) == abs(row[x] - row[i])):
            return False
    return True

def queen(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                queen(x + 1)

queen(0)
print(ans)