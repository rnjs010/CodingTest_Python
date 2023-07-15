n, m = map(int, input().split())
li = sorted([*map(int, input().split())])

def perm(arr):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(n):
        if li[i] not in arr:
            arr.append(li[i])
            perm(arr)
            arr.pop()

perm([])