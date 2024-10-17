class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat[0]) * len(mat): # check for invalidity
            return mat

        mati, matj, resi, resj = 0,0,0,0
        res = [[0 for col in range(c)] for row in range(r)]
        while resi < len(res) and resj < len(res[0]):
            res[resi][resj] = mat[mati][matj]
            matj += 1
            if matj == len(mat[0]):
                matj = 0
                mati += 1
            resj += 1
            if resj == len(res[0]):
                resj = 0
                resi += 1

        return res

'''
TLDR: First, check for validity, which is when r * c == len(mat[0]) * len(mat) (must be equivalent). If not return mat.
Else, we have four variables to keep track of matrix indices. We have if conditions to shift to the next row for both, else we just shift the col (j) index to the right.

TC O(n*m), for n rows and m cols
SC O(1), not counting the resulting matrix.
'''
            
