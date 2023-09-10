import sys
input = sys.stdin.readline

n = input()
f = int(input())
num = int(n)
num -= (num % (10**2))
for i in range(num, num+100, 1):
    if i % f == 0:
        print(f'{(i-num):02d}')
        break