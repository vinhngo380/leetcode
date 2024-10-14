class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # EXCELLENT PROBLEM FOR LEARNING MATRIX TRANSPOSITION
        '''
        Convenient, concise but temp uses extra memory
        matrix[:] = [[matrix[col][row] for col in range(len(matrix[0]))] for row in range(len(matrix))]
        '''
        # Performs in place swaps. NOTE: LOWER BOUND IN second loop!!!
        for row in range(len(matrix)):
            for col in range(row+1, len(matrix[0])): # can also be just matrix due to nxn, ROW +1 as lower bound due to avoiding duplicates across the main diag.
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        for row in matrix: # Reverse to get the 90 deg rotation.
            row.reverse()

        # no return, do in place

        '''
        All Rotations:
        90 deg = transpose + reverse row
        180 deg = reverse row + reverse column
        270 deg = transpose + reverse col
        360 deg = dont do anything :)
        '''

'''
TLDR: Transpose matrix, then reverse rows. More evident if you do it on pen + paper

TC O(n^2)
SC O(1)
'''
