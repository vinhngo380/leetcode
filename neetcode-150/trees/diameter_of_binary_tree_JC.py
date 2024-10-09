class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        # wtf is testcase 106????????? Easy my ass!
        # This too??????????????????!!!!!!!!!!!!!!!
        '''
        [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
        '''
        
        def dfs(root):
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            self.diameter = max(self.diameter, l+r)
            return max(l,r) + 1
        
        dfs(root)
        return self.diameter

'''
TLDR: Should be classified as medium+. Use global variable diameter, and add up the heights of left + right subtrees at each node. 
May be hard to debug if you misplace the +1 somewhere else.

TC O(n)
SC O(h) where h is the height of the tree



    
