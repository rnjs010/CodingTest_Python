pos = ['^', '>', 'v', '<']
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]   # 상우하좌


def move(d):
    global x, y
    board[x][y] = pos[d]
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == '.':
        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
        x, y = nx, ny


T = int(input())
for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    N = int(input())
    command = input()

    x, y = 0, 0
    for i in range(H):  # 현재 위치 찾기
        for j in range(W):
            if board[i][j] in pos:
                x, y = i, j

    for cmd in command: # 명령
        if cmd == 'U':
            move(0)
        elif cmd == 'R':
            move(1)
        elif cmd == 'D':
            move(2)
        elif cmd == 'L':
            move(3)
        else:
            idx = pos.index(board[x][y])
            bomb_x, bomb_y = x + dx[idx], y + dy[idx]
            while True:
                if (not 0 <= bomb_x < H) or (not 0 <= bomb_y < W):
                    break
                if board[bomb_x][bomb_y] == '#':
                    break
                if board[bomb_x][bomb_y] == '*':
                    board[bomb_x][bomb_y] = '.'
                    break
                bomb_x, bomb_y = bomb_x + dx[idx], bomb_y + dy[idx]

    print(f'#{test_case}', end=' ')
    for i in board:
        print(''.join(i))