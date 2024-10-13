class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while top < bottom and left < right:
            # get all i in top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1 # move top boundary down

            # get all i in right-most col
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1 # move right boundary to the left

            if not (left < right and top < bottom):
                break
            
            # get all i in bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1 # move bottom boundary up

            # get all i in left-most col
            for i in range(bottom - 1, top -1, -1):
                res.append(matrix[i][left])
            left += 1 # move left boundary to the right

        return res


'''
TLDR: We use the concepts of "boundaries" here - top, bottom, left, right. Note how the right and bottom bounds are set at the +1 index -> this due to the nature of for loops
Remember that we will need four for loops here, each for each side of the spiral while we move in. There is a conditional in the middle to catch if we are indeed at the middle (nowhere else to go),
BEFORE we attempt to start going down again. This spiral addresses L->R, T->B.

TC O(m * n) -> for m rows and n cols
SC O(1) -> excluding the res matrix
'''
