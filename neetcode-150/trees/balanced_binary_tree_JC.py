class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            if abs(l-r) > 1:
                self.balanced = False
            
            return max(l,r) + 1
        
        dfs(root)
        return self.balanced


'''
TLDR: Use dfs to find the height of the left and right subtrees, then compare.  If the difference is ever greater than 1, then the global variable self.balance = False, otherwise True.
Note that the global variable may not be needed.

TC O(n)
SC O(h) - O(logn) best, O(n) worst.
'''
