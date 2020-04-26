while 1:
    def numIslands(grid):
        cnt = 0
        check = 1
        if len(grid) == 0:
            return 0
        for i in range(len(grid)):
            grid[i] = [0] + list(grid[i]) + [0]
        grid = [[0 for _ in range(len(grid[0]))]] + grid + [[0 for _ in range(len(grid[0]))]]
        def sarch_island(grid, nowi, nowj, s):
            # print(nowi, nowj, grid)
            grid[nowi][nowj] = 0
            s += 1
            if grid[nowi - 1][nowj] == 1:
                grid = sarch_island(grid, nowi - 1, nowj, s)
            if grid[nowi + 1][nowj] == 1:
                grid = sarch_island(grid, nowi + 1, nowj, s)
            if grid[nowi][nowj - 1] == 1:
                grid = sarch_island(grid, nowi, nowj - 1, s)
            if grid[nowi][nowj + 1] == 1:
                grid = sarch_island(grid, nowi, nowj + 1, s)
            return grid, s

        ans = 0
        print(grid)
        while check:
            check = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    print(grid[i][j])
                    if grid[i][j] == 1:
                        print(i, j, 0)
                        check = 1
                        cnt += 1
                        grid, this_s = sarch_island(grid, i, j, 0)
                        ans = max(ans, this_s)

        return ans

    grid = [[1, 1, 1]]
    print(numIslands(grid))
    break