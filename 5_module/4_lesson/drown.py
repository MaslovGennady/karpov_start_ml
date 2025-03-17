def drown(board):
    if not board:
        return board

    m, n = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Функция для BFS
    def bfs(i, j):
        queue = [(i, j),]
        board[i][j] = '#'  # Помечаем как не подлежащий затоплению
        
        while queue:
            x, y = queue[0]
            queue = queue[1:]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                    board[nx][ny] = '#'  # Помечаем как не подлежащий затоплению
                    queue.append((nx, ny))

    # BFS для всех 'O' на краях
    for i in range(m):
        for j in range(n):
            if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and board[i][j] == 'O':
                bfs(i, j)

    # Затопляем остальные 'O'
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'  # Затопляем
            elif board[i][j] == '#':
                board[i][j] = 'O'  # Возвращаем обратно

    return board