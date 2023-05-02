from itertools import permutations
n = int(input())
li = list(permutations(range(1, n+1), n))
for i in sorted(li):
    print(' '.join(map(str, i)))