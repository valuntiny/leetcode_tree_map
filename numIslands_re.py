'''
Quest:
    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    You may assume all four edges of the grid are all surrounded by water.

    Example 1:
    Input:
    11110
    11010
    11000
    00000
    Output: 1

    Example 2:
    Input:
    11000
    11000
    00100
    00011
    Output: 3

Solution:
    - spreading the virus
'''

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.helper(grid, i, j)

        return res

    def helper(self, grid, i, j):
        if i not in range(len(grid)) or j not in range(len(grid[0])) or grid[i][j] != "1":
            return

        grid[i][j] = "2"
        self.helper(grid, i-1, j)
        self.helper(grid, i+1, j)
        self.helper(grid, i, j-1)
        self.helper(grid, i, j+1)