# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #perform DFS
        #:( idk how i couldnt figure this out
        if not root:
            return 0
        return  1 + self.maxDepth(root.left) + self.maxDepth(root.right)
