#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """
    visit = set()
    def dfs(i, j):
        if i >= length(grid) or j >= length(grid[0]) or \
                i < 0 or j < 0 or grid[i][j] == 0 :
                    return 1
        if (i ,j) in visit:
            return 0
        visit.add((i, j))
        perimitar = dfs(i - 1,j)
        perimitar += dfs(i + 1,j)
        perimitar += dfs(i, j - 1)
        perimitar += dfs(i, j + 1)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j);
