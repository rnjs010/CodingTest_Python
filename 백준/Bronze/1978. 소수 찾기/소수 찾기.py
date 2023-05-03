n = int(input())
li = [int(i) for i in input().split()]

def check(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

sum = 0
for i in li:
    if check(i) == True:
        sum += 1
print(sum)