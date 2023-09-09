import sys
input = sys.stdin.readline

n = int(input())
li = [*map(int, input().split())]
li.sort()
print(li[n // 2 - 1] if n % 2 == 0 else li[n // 2])