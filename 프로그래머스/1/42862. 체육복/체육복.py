def solution(n, lost, reserve):
    reserve_u = [r for r in reserve if r not in lost]
    reserve_u.sort()
    lost_u = [l for l in lost if l not in reserve]
    lost_u.sort()
    for i in reserve_u:
        if i-1 in lost_u:
            lost_u.remove(i-1)
        elif i+1 in lost_u:
            lost_u.remove(i+1)
    answer = n - len(lost_u)
    return answer