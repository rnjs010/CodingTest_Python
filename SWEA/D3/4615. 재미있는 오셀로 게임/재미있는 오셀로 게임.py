dx, dy = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N // 2][N // 2], board[N // 2 - 1][N // 2 - 1] = 2, 2
    board[N // 2 - 1][N // 2], board[N // 2][N // 2 - 1] = 1, 1
    for _ in range(M):
        y, x, c = map(int, input().split())
        x, y = x - 1, y - 1
        board[x][y] = c
        for k in range(8):
            for i in range(1, N):
                nx, ny = x + (dx[k] * i), y + (dy[k] * i)
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] == c:
                        for j in range(1, i):
                            cx, cy = x + (dx[k] * j), y + (dy[k] * j)
                            if board[cx][cy] != 0:  board[cx][cy] = c
                        break
                    elif board[nx][ny] == 0:
                        break
                        
    B_cnt, W_cnt = 0, 0
    for i in board:
        B_cnt += i.count(1)
        W_cnt += i.count(2)

    print(f'#{tc} {B_cnt} {W_cnt}')
