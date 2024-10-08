class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root): # Not necessary, could use on self.invertTree but I am used to this for later inverting.
            if not root:
                return
            temp = root.left
            root.left = root.right
            root.right = temp
            invert(root.left)
            invert(root.right)
        invert(root)
        return root


'''
TLDR: Define an invert function (not necessary), which sets root.left = root.right and vice versa, then recursively calls it on the root.left and root.right.
Base case if root is None.

TC O(n)
SC O(H)
'''
