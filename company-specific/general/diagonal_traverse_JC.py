class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res, isUp = [], True
        i, j = 0, 0
        while len(res) < (len(mat) * len(mat[0])):
            if isUp:
                while i >= 0 and j < len(mat[0]):
                    res.append(mat[i][j]) 
                    i -= 1
                    j += 1
                if i < 0 and j < len(mat[0]): # condition to move back to row (i += 1)
                    i += 1
                else:
                    i += 2
                    j -= 1
                isUp = False
            else:
                while i < len(mat) and j >= 0:
                    res.append(mat[i][j])
                    i += 1
                    j -= 1
                if j < 0 and i < len(mat): # condition to move back to col (j += 1)
                    j += 1
                else:
                    j += 2
                    i -= 1
                isUp = True
        return res
'''
TLDR: Conceptually manageable to come up with a solution, but tricky to handle the traversals. We need 4 conditions, 2 each for diag up/left traversal and down/right traversal.
The first two (for up/left) is as follows: goes out of bonuds BUT still in the col, or goes OUT of both bounds. 
The other two (for down/right) is as follows: goes out of bounds BUT still in row, or goes OUT of both bounds.
For all four, we need to modify the indexes as such, above.

TC O(m * n)
SC O(1) - not counting the output matrix
'''

        
