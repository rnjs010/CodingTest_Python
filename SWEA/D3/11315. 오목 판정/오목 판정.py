dx, dy = [0, 1, 1, 1], [1, 1, 0, -1]
def check():
    for x in range(N):
        for y in range(N):
            if board[x][y] == 'o':
                for k in range(4):
                    for i in range(1, 5):
                        nx, ny = x + (dx[k] * i), y + (dy[k] * i)
                        if not (0 <= nx < N) or not (0 <= ny < N) or not (board[nx][ny] == 'o'):
                            break
                    else:
                        return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]
    ans = check()
    print(f'#{tc} {ans}')