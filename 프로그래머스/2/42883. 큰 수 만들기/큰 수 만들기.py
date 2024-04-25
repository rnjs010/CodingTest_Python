def solution(number, k):
    answer = []
 
    for num in number:
        while k > 0 and answer and num > answer[-1]:
            answer.pop()
            k -= 1
        answer.append(num)

    answer = ''.join(answer[:len(answer) - k])
    return answer