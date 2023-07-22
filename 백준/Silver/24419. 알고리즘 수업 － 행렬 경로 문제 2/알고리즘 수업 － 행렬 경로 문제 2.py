import math
n = int(input())
m = [[*map(int, input().split())] for _ in range(n)]
print((math.factorial(2*n) // math.factorial(n)**2)%1000000007, n**2)