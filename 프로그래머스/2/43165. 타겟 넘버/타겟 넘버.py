global cnt
cnt = 0
def dfs(nums, t, idx, total, x):
    global cnt
    total += nums[idx] * x
    if idx == len(nums) - 1:
        if total == t:
            cnt += 1
    else:
        dfs(nums, t, idx+1, total, 1)
        dfs(nums, t, idx+1, total, -1)
    return cnt
    
def solution(numbers, target):
    dfs(numbers, target, 0, 0, 1)
    answer = dfs(numbers, target, 0, 0, -1)
    return answer