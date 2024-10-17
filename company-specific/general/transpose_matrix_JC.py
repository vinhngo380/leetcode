class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [] 
        for j in range(len(matrix[0])):
            curr = []
            for i in range(len(matrix)):
                curr.append(matrix[i][j])
            res.append(curr)
        return res


'''
TLDR: Note we cannot use the square in-place transpose for this problem due to the matrix being n * m size.
Instead, we can see the pattern where for each row in ex: res[0], it will be the [matrix[i][0], matrix[i+1][0]...].
The second row will res[1] = [matrix[i][1], matrix[i+1][1]...] and so on.

TC O(n*m)
SC O(n*m)
'''

        
