k = int(input())
li = input().split()
ans = []
arr = []
def perm(x):
    global arr
    if x == k:
        ans.append(''.join(map(str, arr)))
        return
    
    for i in range(10):
        if i not in arr:
            if (li[x] == '<' and arr[-1] < i) or (li[x] == '>' and arr[-1] > i):
                arr.append(i)
                perm(x + 1)
                arr.pop()

for i in range(10):
    arr.append(i)
    perm(0)
    arr.pop()
ans.sort()
print(ans[-1])
print(ans[0])