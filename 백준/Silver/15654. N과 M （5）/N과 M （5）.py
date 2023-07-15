n, m = map(int, input().split())
li = sorted([*map(int, input().split())])
used = [0] * n
def perm(arr):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(n):
        if used[i] == 0:
            used[i] = 1
            perm(arr + [li[i]])
            used[i] = 0

perm([])