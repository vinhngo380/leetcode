class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        curr = 1
        matrix = [[x for x in range(n)] for y in range(n)] # USE List Comprehension to create nxn matrix. [[0] *n] * n will create duplicate lists
        left, right = 0, n
        top, bottom = 0, n
        while top < bottom and left < right:
            # set all is in top row
            for i in range(left, right):
                matrix[top][i] = curr
                curr += 1
            top += 1

            # set all is in right column
            for i in range(top, bottom):
                matrix[i][right-1] = curr
                curr += 1
            right -= 1

            if not (top < bottom and left < right):
                break

            # set all is in bottom row
            for i in range(right-1, left-1, -1):
                matrix[bottom-1][i] = curr
                curr += 1
            bottom -= 1

            # set all is in left col
            for i in range(bottom-1, top-1, -1):
                matrix[i][left] = curr
                curr += 1
            left += 1

        return matrix


'''
TLDR: Same exact process as spiral matrix 1, but we are setting instead of getting an appending to res.

TC O(n^2)
SC O(n^2)
'''
