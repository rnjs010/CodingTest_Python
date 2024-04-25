def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    ans = [0,0,0,0]
    for i in range(len(answers)):
        if p1[i%len(p1)] == answers[i]:
            ans[1] += 1
        if p2[i%len(p2)] == answers[i]:
            ans[2] += 1
        if p3[i%len(p3)] == answers[i]:
            ans[3] += 1

    answer = list(filter(lambda x: ans[x] == max(ans), range(1,len(ans))))

    return answer