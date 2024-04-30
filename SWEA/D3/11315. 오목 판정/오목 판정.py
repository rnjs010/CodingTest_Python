dx, dy = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]
    ans = 'NO'
    for x in range(N):
        for y in range(N):
            if board[x][y] == 'o':
                for k in range(8):
                    for i in range(1, 5):
                        nx, ny = x + (dx[k] * i), y + (dy[k] * i)
                        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 'o':
                            continue
                        else:
                            break
                    else:
                        ans = 'YES'
                        break
        
    print(f'#{tc} {ans}')
