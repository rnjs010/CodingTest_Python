import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip()
    st = []
    m = 0
    for i in s:
        if i == '[':
            st.append(i)
        else:
            st.pop()
        m = max(m, len(st))
    print(2**m)