class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root): # Not necessary, can call recursively on maxDepth itself, but I prefer to define dfs for later problems.
            if not root:
                return 0
            l = 1 + dfs(root.left)
            r = 1 + dfs(root.right)
            
            return max(l,r)

        return dfs(root)

'''
TLDR: Recursively call the dfs function, which goes through the tree and finds the max depth of each l,r and returns that.

TC O(n) - Goes through all nodes in the tree
SC O(n) - Calls O(n) functions and takes up O(n) space in the call stack
'''
  
