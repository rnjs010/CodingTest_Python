def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        array_c = array[commands[i][0]-1:commands[i][1]]
        array_c.sort()
        answer.append(array_c[commands[i][2]-1])
    return answer