def min_path(grid):
    
    if grid is None or len(grid) == 0 or grid[0] is None or len(grid[0]) == 0:
        return None
    
    for i in range(1, len(grid[0])):
        grid[0][i] = grid[0][i] + grid[0][i-1]
        #p_print(grid, '')
    
    for i in range(1, len(grid)):
        grid[i][0] = grid[i][0] + grid[i-1][0]
        #p_print(grid, '')
    
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + grid[i][j]
            # p_print(grid, '')
    
    return grid[len(grid) - 1][len(grid[0]) - 1]