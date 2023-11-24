def solution(s):
    ans = []
    li = s[2:-1].replace('},{', '/')
    li = li[:-1].split('/')
    li.sort(key= lambda x: len(x))

    for i in range(len(li)):
        li[i] = li[i].split(',')

    ans.append(int(li[0][0]))
    for i in range(1,len(li)):
        j = list(set(li[i])-set(li[i-1]))
        ans.append(int(j[0]))
    return ans