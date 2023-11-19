l, r = input().rstrip().split()
if '8' not in l or '8' not in r or len(l) != len(r):
    print(0)
else:
    cnt = 0
    for i in range(len(l)):
        if l[i] == '8' and r[i] == '8':
            cnt += 1
        if l[i] != r[i]:
            print(cnt)
            break
    else:
        print(cnt)