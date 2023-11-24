from collections import deque

def solution(queue1, queue2):
    ans = 0
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    if ((s1 + s2) % 2) != 0:
        return -1
    for _ in range(len(q1)*3 + 1):
        if s1 == s2:
            break
        elif s2 < s1:
            s1 -= q1[0]
            s2 += q1[0]
            q2.append(q1.popleft())
            ans += 1
            
        elif s2 > s1:
            s2 -= q2[0]
            s1 += q2[0]
            q1.append(q2.popleft())
            ans += 1
    else:
        return -1
    
    return ans