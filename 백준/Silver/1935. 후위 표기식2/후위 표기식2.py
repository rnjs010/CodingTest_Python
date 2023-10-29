import math
import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
d = dict()
for i in range(n):
    d[chr(ord('A')+i)] = int(input())

st = []
for i in s:
    if ord('A') <= ord(i) <= ord('Z'):
        st.append(d[i])
    else:
        b = str(st.pop())
        a = str(st.pop())
        st.append(f'{eval(a + i + b):.2f}')

print(st[0])