class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q): # Do not have to use a dfs function, can just call isSameTree recursively.
            if not p and not q:
                return True
            elif (p and not q) or (not p and q):
                return False
            
            l = dfs(p.left, q.left)
            r = dfs(p.right, q.right)

            return (l and r) and (p.val == q.val)

        return dfs(p,q)

'''
TLDR: Use dfs to compare the l and r, as well as the p == q.

TC O(n)
SC O(h)
'''
