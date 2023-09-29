import sys
input = sys.stdin.readline
n, m = map(int, input().split())

day = {0:'SUN', 1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT'}
d = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
if n == 1:
    print(day[m % 7])
else:
    for i in range(1,n):
        m += d[i]
    print(day[m % 7])