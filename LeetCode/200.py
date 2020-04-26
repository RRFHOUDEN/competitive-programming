while 1:
    def numIslands(grid):
        cnt = 0
        check = 1
        if len(grid) == 0:
            return 0
        for i in range(len(grid)):
            grid[i] = ["0"] + list(grid[i]) + ["0"]
        grid = [["0" for _ in range(len(grid[0]))]] + grid + [["0" for _ in range(len(grid[0]))]]
        def sarch_island(grid, nowi, nowj):
            # print(nowi, nowj, grid)
            grid[nowi][nowj] = "0"
            if grid[nowi - 1][nowj] == "1":
                grid = sarch_island(grid, nowi - 1, nowj)
            if grid[nowi + 1][nowj] == "1":
                grid = sarch_island(grid, nowi + 1, nowj)
            if grid[nowi][nowj - 1] == "1":
                grid = sarch_island(grid, nowi, nowj - 1)
            if grid[nowi][nowj + 1] == "1":
                grid = sarch_island(grid, nowi, nowj + 1)
            return grid

        while check:
            check = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == "1":
                        print(i, j)
                        check = 1
                        cnt += 1
                        grid = sarch_island(grid, i, j)

        return cnt

    grid = []
    print(numIslands(grid))
    break