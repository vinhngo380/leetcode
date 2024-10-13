# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        #find middle, make that the pivot point then recursively
        #reverse 1st half of the pivot
        #iterate through 1st half and 2nd half
        cache = [] 
        current = head
        if not head:
            return None

        while current:
            cache.append(current.val)
            current = current.next
        pivot_index = len(cache) // 2
        return self.create_tree(cache[pivot_index], cache)
    
    def create_tree(self, array):
        if not array:
            return None

        if len(array) < 3
            pivot_index = len(array) // 2
            pivot = array[pivot_index]
        else:
            pivot_index = len(array) // 2
            pivot = array[pivot_index]
            return TreeNode(
                pivot, 
                left = create_tree(array[::pivot_index], ),
                right = create_tree(array[pivot_index::-1])
            )
#this code is not finished
