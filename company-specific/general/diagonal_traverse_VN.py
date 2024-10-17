class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        height, width = len(mat), len(mat[0])
        result = []
        numDiag = 1
        while i < height and j < width:
            #getting diagonial
            if numDiag % 2 == 0:
                temp, temp2 = i, j
                while i > 0 and j > 0:
                    result.append(mat[i][j])
                    i -= 1
                    j -= 1
                i = height - 1
                j = 0
                numDiag += 1
            if numDiag % 2 == 1:
                while i < height and j < width:
                    result.append(mat[i][j])
                    i += 1
                    j += 1
                i = 0
                j = width - 1
                numDiag += 1
        return result
