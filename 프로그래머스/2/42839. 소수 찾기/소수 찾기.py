from itertools import permutations

def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    all = []
    for i in range(1, len(numbers)+1):
        ans = list(permutations(numbers, i))
        for j in range(len(ans)):
            num = int(''.join(ans[j]))
            if isprime(num):
                all.append(num)

    remove_set = {0, 1}      # 0, 1 제거
    all = [i for i in all if i not in remove_set]

    my_set = set(all)       # 중복 제거
    all = list(my_set)

    return len(all)