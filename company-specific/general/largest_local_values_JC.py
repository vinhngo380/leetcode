class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = [[0 for c in range(len(grid)-2)] for r in range(len(grid)-2)]
        i, j = 1,1
        resi, resj = 0, 0
        # for the loops, we have to have some "padding"
        while i < len(grid) - 1 and j < len(grid) - 1:
            # top row of 3x3
            topL, topM, topR = grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1]
            # mid row of 3x3
            midL, midM, midR = grid[i][j-1], grid[i][j], grid[i][j+1]
            # bottom row of 3x3
            botL, botM, botR = grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]
            res[resi][resj] = max(topL, topM, topR, midL, midM, midR, botL, botM, botR)
            resj += 1
            if resj == len(res[0]):
                resi += 1
                resj = 0
            j += 1
            if j == len(grid[0]) - 1:
                i += 1
                j = 1
        return res

'''
TLDR: Essentially, we are comparing every value in a 3x3 subgrid. To do so, we have a padding of 1 on all sides of the grid for our while loop.
To find the max, we take the max(...) of every possible value in the 3x3 subgrid. Note that when we go "reset" the indexes, we maintain the padding for i and j.

TC O(n^2)
SC O(n^2)
'''
