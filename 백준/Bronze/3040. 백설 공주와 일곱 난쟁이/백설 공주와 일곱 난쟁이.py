li = [int(input()) for i in range(9)]
for i in range(8):
    for j in range(i+1, 9):
        if sum(li) - li[i] - li[j] == 100:
            for z in range(9):
                if z not in [i, j]:
                    print(li[z])
            break