from itertools import combinations

while True:
    li = [*map(int, input().split())]
    if li == [0]:
        break

    for i in [*combinations(li[1:], 6)]:
        print(*i)
    print()