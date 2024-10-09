# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #slow and fast pointer
        #until the slow pointer is out of bounds
        #iterate through until they have the same # and return
        #TC: O(n) - it will only iterate through the whole
        #LL once, but if not, it will just keep cycling until
        #they are the same, which will still be O(cn) = O(n) time
        #SC: O(1) - only dummy head
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False 

        

