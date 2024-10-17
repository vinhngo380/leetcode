# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #use DFS to see which value is the highest
    #but idk how to backtrack to the root node, maybe max() & recursion?
    #TC: O(N) since you have to go through all the nodes
    #SC: O(1) unless you count the stack frame
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #perform DFS
        if root is None: 
            return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
    

