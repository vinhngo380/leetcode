class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i < len(matrix) -1 and j < len(matrix[0]) - 1:
                    if matrix[i][j] != matrix[i+1][j+1]:
                        return False
        return True

'''
TLDR: The pattern (recognizable from the array) is matrix[i][j] == matrix[i+1][j+1] for it to be a Toeplitz Matrix (all top-left to bottom-right diags are the same element).

TC O(n*m), where n == rows, m == cols
SC (1)
'''
